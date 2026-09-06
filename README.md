# 📑 TaxAuditAI: Two-Stage Machine Learning Pipeline for Tunisian Tax Fraud Detection

An end-to-end data engineering and machine learning framework designed to identify non-compliant tax filings and predict corporate audit penalties using relational data staging, domain feature engineering, and a two-stage gradient boosting architecture.

---

## 🚀 Overview

This project analyzes corporate tax declaration records from the **Tunisian Tax Fraud Detection Dataset** to predict financial penalties resulting from tax discrepancies.

It combines:

* **Relational Data Engineering**: Automated ingestion, schema auditing, and data staging in MySQL
* **Advanced Data Cleaning**: Systematic treatment of structural `NULL` values and zero-variance feature removal
* **Domain Feature Engineering**: Financial ratios, TVA-to-turnover discrepancies, and cross-declaration variance signals
* **Two-Stage Machine Learning**: Binary classification (zero vs. non-zero target) paired with specialized regression for zero-inflated continuous targets

---

## 🧠 Key Features

* 🗄️ **MySQL Staging Pipeline**: High-throughput ingestion and structured validation for large-scale tax declaration records
* 🧹 **Data Quality Auditing**: Identification and purging of 12 zero-variance constant features across 120+ raw attributes
* 📊 **Domain-Specific Ratios**: Extraction of financial indicators from sparse invoice logs and tax obligation codes (`CTR_OBL*`)
* ⚡ **Two-Stage Architecture**: Classification Stage (Compliant vs. Non-Compliant) → Regression Stage (Penalty Amount Prediction)
* 📈 **Zero-Inflated Loss Optimization**: Gradient boosting algorithms (XGBoost / LightGBM) calibrated for heavy zero-density target distributions

---

## 🛠️ Tech Stack

* **Language**: Python
* **Database Engine**: MySQL 8.0, SQLAlchemy
* **Data Engineering**: Pandas, NumPy, SciPy
* **Machine Learning**: XGBoost, LightGBM, Scikit-Learn
* **Visualization**: Matplotlib, Seaborn

---

## 📂 Project Structure

```text
TaxAuditAI/
│
├── data/                      # Dataset files (raw & processed)
│   ├── raw/                   # Train.csv and Test.csv
│   └── processed/             # Cleaned features & engineered tables
│
├── sql/                       # Database scripts
│   ├── 01_schema_setup.sql    # MySQL database and table schemas
│   └── 02_data_audit.sql      # Queries for missingness & variance checks
│
├── notebooks/                 # Exploratory data analysis & modeling
│   ├── 01_eda_and_mysql_staging.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_two_stage_model_training.ipynb
│
├── src/                       # Core source code
│   ├── db_connection.py       # Database connector setup
│   ├── preprocessing.py       # Data cleaning & ratio calculations
│   └── model_pipeline.py      # Two-stage inference pipeline
│
├── models/                    # Saved model artifacts
│   ├── classifier_stage1.pkl
│   ├── regressor_stage2.pkl
│   └── scaler_and_encoder.pkl
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline Flow

Data Ingestion → MySQL Staging → Data Audit & Cleansing → Feature Engineering → Two-Stage Modeling → Audit Penalty Output

---

## 📌 Dataset & Source

* **Dataset**: Tunisian Tax Fraud Detection Dataset (Zindi / Enterprise Tax Declaration Records)
* **Training Set**: 21,295 entries | 121 features
* **Testing Set**: 7,517 entries | 120 features
* **Target Distribution**: Continuous discrepancy amount (`target`) with 5,402 entries (25.37%) at exactly zero (compliant/non-penalized)

---

## 🎯 Use Cases

* **Tax Audit Prioritization**: Automated triage of tax declarations to identify high-risk corporate filers
* **Compliance Monitoring**: Early warning systems for financial discrepancies and invoice misalignments
* **Resource Optimization**: Channeling tax authority field operations toward high-value potential recoveries
* **Fraud Analytics**: Uncovering structural anomalies across import/export and TVA reporting channels

---

## 🧠 Future Improvements

* **Explainable AI**: Integration of SHAP values for feature-level audit justifications
* **Automated SQL Pipeline**: Airflow orchestration for end-to-end staging and model scoring
* **Real-Time API**: FastAPI deployment for instant declaration scoring
* **Graph Neural Networks**: Inter-company transaction networks for VAT evasion detection

---

## 👤 Author

**Tanmoy Pal**  
