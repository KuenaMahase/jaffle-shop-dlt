import dlt
import os
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.paginators import PageNumberPaginator
import time

# ----------------------------
# API and Client Configuration
# ----------------------------
API_BASE = "https://jaffle-shop.scalevector.ai/api/v1"
client = RESTClient(
    base_url=API_BASE,
    paginator=PageNumberPaginator(
        base_page=1,
        page_param="page",
        total_path=None,
        stop_after_empty_page=True
    )
)

# ----------------------------
# Environment Variables for Performance Tuning
# ----------------------------
os.environ['EXTRACT__WORKERS'] = '8'
os.environ['NORMALIZE__WORKERS'] = '4'
os.environ['LOAD__WORKERS'] = '4'
os.environ['DATA_WRITER__DISABLE_COMPRESSION'] = 'true'
os.environ['DATA_WRITER__BUFFER_MAX_ITEMS'] = '5000'
os.environ['DATA_WRITER__FILE_MAX_ITEMS'] = '2000'

# ----------------------------
# Resource Definitions
# ----------------------------
@dlt.resource(
    table_name="customers",
    write_disposition="append",
    primary_key="id",
    parallelized=True
)
def get_customers():
    """Fetch all customers in chunks of 500"""
    yield from client.paginate("/customers", params={"page_size": 500})

@dlt.resource(
    table_name="orders",
    write_disposition="append",
    primary_key="id",
    parallelized=True
)
def get_orders():
    """Fetch all orders in chunks of 1000"""
    yield from client.paginate("/orders", params={"page_size": 1000})

@dlt.resource(
    table_name="products",
    write_disposition="append",
    primary_key="sku",
    parallelized=True
)
def get_products():
    """Fetch all products in chunks of 100"""
    yield from client.paginate("/products", params={"page_size": 100})

# ----------------------------
# Grouped Source Definition
# ----------------------------
@dlt.source(name="jaffle_shop_source")
def jaffle_shop_source():
    """Group customers, orders, and products resources into one source"""
    return [get_customers(), get_orders(), get_products()]

# ----------------------------
# Pipeline Setup and Execution
# ----------------------------
def main():
    pipeline = dlt.pipeline(
        pipeline_name="optimized_jaffle_pipeline",
        destination="duckdb",
        dataset_name="optimized_jaffle_data",
        #dev_mode=true
    )
    start = time.time()
    load_info = pipeline.run(jaffle_shop_source())
    duration = time.time() - start
    print(f"Total Pipeline Duration: {duration:.2f} seconds")
    print(pipeline.last_trace)

if __name__ == "__main__":
    main()