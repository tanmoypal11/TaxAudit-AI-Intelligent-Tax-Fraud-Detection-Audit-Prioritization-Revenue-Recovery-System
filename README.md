📑 TaxAuditAI: Two-Stage Machine Learning Pipeline for Tunisian Tax Fraud DetectionAn end-to-end data engineering and machine learning framework designed to identify non-compliant tax filings and predict corporate audit penalties using relational data staging, domain feature engineering, and a two-stage gradient boosting architecture.🚀 OverviewThis project analyzes corporate tax declaration records from the Tunisian Tax Fraud Detection Dataset to predict financial penalties resulting from tax discrepancies.It combines:Relational Data Engineering: Automated ingestion, schema auditing, and data staging in MySQLAdvanced Data Cleaning: Systematic treatment of structural NULL values and zero-variance feature removalDomain Feature Engineering: Financial ratios, TVA-to-turnover discrepancies, and cross-declaration variance signalsTwo-Stage Machine Learning: Binary classification (zero vs. non-zero target) paired with specialized regression for zero-inflated continuous targets🧠 Key Features🗄️ MySQL Staging Pipeline: High-throughput ingestion and structured validation for large-scale tax declaration records🧹 Data Quality Auditing: Identification and purging of 12 zero-variance constant features across 120+ raw attributes📊 Domain-Specific Ratios: Extraction of financial indicators from sparse invoice logs and tax obligation codes (CTR_OBL*)⚡ Two-Stage Architecture: Classification Stage (Compliant vs. Non-Compliant) $\rightarrow$ Regression Stage (Penalty Amount Prediction)📈 Zero-Inflated Loss Optimization: Gradient boosting algorithms (XGBoost / LightGBM) calibrated for heavy zero-density target distributions🛠️ Tech StackLanguage: PythonDatabase Engine: MySQL 8.0, SQLAlchemyData Engineering: Pandas, NumPy, SciPyMachine Learning: XGBoost, LightGBM, Scikit-LearnVisualization: Matplotlib, Seaborn📂 Project StructurePlaintextTaxAuditAI/
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
⚙️ Pipeline FlowData Ingestion $\rightarrow$ MySQL Staging $\rightarrow$ Data Audit & Cleansing $\rightarrow$ Feature Engineering $\rightarrow$ Two-Stage Modeling $\rightarrow$ Audit Penalty Output📌 Dataset & SourceDataset: Tunisian Tax Fraud Detection Dataset (Zindi / Enterprise Tax Declaration Records)Training Set: 21,295 entries | 121 featuresTesting Set: 7,517 entries | 120 featuresTarget Distribution: Continuous discrepancy amount (target) with 5,402 entries (25.37%) at exactly zero (compliant/non-penalized)🎯 Use CasesTax Audit Prioritization: Automated triage of tax declarations to identify high-risk corporate filersCompliance Monitoring: Early warning systems for financial discrepancies and invoice misalignmentsResource Optimization: Channeling tax authority field operations toward high-value potential recoveriesFraud Analytics: Uncovering structural anomalies across import/export and TVA reporting channels🧠 Future ImprovementsExplainable AI: Integration of SHAP values for feature-level audit justificationsAutomated SQL Pipeline: Airflow orchestration for end-to-end staging and model scoringReal-Time API: FastAPI deployment for instant declaration scoringGraph Neural Networks: Inter-company transaction networks for VAT evasion detection👤 AuthorTanmoy Pal