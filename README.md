```markdown
# Jaffle Shop DLT Pipeline

This project demonstrates how to deploy a **data pipeline** using [`dlt`](https://github.com/dlt-hub/dlt) and **GitHub Actions** for automation. It extracts, normalizes, and loads data from a sample Jaffle Shop API into a local DuckDB database.

---

## Project Overview

- **Language:** Python  
- **Pipeline Tool:** dlt (Data Loading Tool)  
- **Destination:** DuckDB (file-based analytical database)  
- **CI/CD:** GitHub Actions  
- **Deployment Schedule:** Every 30 minutes via cron

---

## Project Structure

```

jaffle-shop-dlt/
├── jaffle\_pipeline.py                        # Main pipeline logic
├── optimized\_jaffle\_pipeline.duckdb          # Output DuckDB database
├── requirements.txt                          # Dependencies for local runs
├── requirements\_github\_action.txt            # Dependencies for GitHub Actions
├── .github/
│   └── workflows/
│       └── run\_optimized\_jaffle\_pipeline\_workflow\.yml  # GitHub Actions workflow
├── .dlt/
│   └── secrets.toml                          # Local config and secrets (excluded from repo)

````

---

## GitHub Secrets

This project uses **GitHub Actions Secrets** to manage configuration securely.

You must set the following secret in your GitHub repository under:  
`Settings > Secrets and variables > Actions`

| Name                           | Example Value                                |
|--------------------------------|----------------------------------------------|
| `DESTINATION__DUCKDB__CREDENTIALS` | `duckdb:///optimized_jaffle_pipeline.duckdb` |

---

## 🚀 Run the Pipeline Locally

```bash
pip install -r requirements.txt
python jaffle_pipeline.py
````

This will fetch and load data into `optimized_jaffle_pipeline.duckdb`.

---

## GitHub Actions Deployment

This project is deployed via GitHub Actions:

* **Auto schedule:** Every 30 minutes (`*/30 * * * *`)
* **Manual trigger:** Supported via GitHub Actions UI

**Run / Monitor workflow:**
[GitHub Actions Workflow](https://github.com/KuenaMahase/jaffle-shop-dlt/actions)

---

##  Completion Checklist

* [x] Local pipeline works
* [x] GitHub repository initialized
* [x] GitHub Actions workflow deployed
* [x] Secrets configured securely
* [x] **Exercise 1 complete**

---

## Author

**Kuena Mahase**
[GitHub Profile →](https://github.com/KuenaMahase)

---

**Note:** This project is part of the **DLT Advanced Course** and is intended for educational purposes.

````

---

###  To Add It to Your Repo:

1. Create the README file:

   ```bash
   nano README.md
````

2. Paste the content above.

3. Save and commit:

   ```bash
   git add README.md
   git commit -m "Add project README"
   git push origin main
   ```

Let me know if you'd like to include a screenshot, badge, or diagram for bonus clarity.
