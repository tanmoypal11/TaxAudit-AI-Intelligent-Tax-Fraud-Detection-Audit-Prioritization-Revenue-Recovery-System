import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.exc import SQLAlchemyError
# ============================================================
# TAXAUDITAI GEMINI AGENT
# ============================================================

import sys
from pathlib import Path

AGENT_PATH = Path(
    r"C:\Users\TANMOY PAL\OneDrive\Desktop\Tunisian Fraud Detection Challenge\data\step24_agent"
)

if str(AGENT_PATH) not in sys.path:
    sys.path.insert(0, str(AGENT_PATH))

import agent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="TaxAuditAI",
    page_icon="🔍",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🔍 TaxAuditAI")
st.subheader("Tunisian Tax Fraud Detection & Audit Intelligence")


# ============================================================
# MYSQL CONNECTION
# ============================================================

@st.cache_resource
def get_database_connection():

    mysql = st.secrets["mysql"]

    # URL.create() safely handles special characters
    # in the MySQL password.
    connection_url = URL.create(
        drivername="mysql+pymysql",
        username=mysql["user"],
        password=mysql["password"],
        host=mysql["host"],
        port=int(mysql["port"]),
        database=mysql["database"]
    )

    engine = create_engine(
        connection_url,
        pool_pre_ping=True
    )

    return engine


# ============================================================
# TEST DATABASE CONNECTION
# ============================================================

try:

    engine = get_database_connection()

    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

    st.success(
        "✅ Connected successfully to TaxAuditAI MySQL database"
    )

except SQLAlchemyError as e:

    st.error(
        "❌ Could not connect to the TaxAuditAI database."
    )

    st.code(str(e))

    st.stop()


# ============================================================
# DATABASE TABLES
# ============================================================

st.header("📊 Database Tables")

try:

    tables = pd.read_sql(
        text("""
            SELECT
                TABLE_NAME,
                TABLE_TYPE
            FROM information_schema.TABLES
            WHERE TABLE_SCHEMA = :database
            ORDER BY TABLE_TYPE, TABLE_NAME
        """),
        engine,
        params={
            "database": "TaxAuditAI"
        }
    )

    st.dataframe(
        tables,
        use_container_width=True,
        hide_index=True
    )

except SQLAlchemyError as e:

    st.error("Could not retrieve database tables.")

    st.code(str(e))


# ============================================================
# TABLE ROW COUNTS
# ============================================================

st.header("📈 Table Summary")

try:

    table_names = tables["TABLE_NAME"].tolist()

    summary = []

    for table in table_names:

        count_query = text(
            f"SELECT COUNT(*) AS row_count "
            f"FROM `{table}`"
        )

        count_df = pd.read_sql(
            count_query,
            engine
        )

        summary.append({
            "Table": table,
            "Rows": int(
                count_df.iloc[0]["row_count"]
            )
        })

    summary_df = pd.DataFrame(summary)

    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )

except Exception as e:

    st.error(
        "Could not calculate table row counts."
    )

    st.code(str(e))


# ============================================================
# CONNECTION INFORMATION
# ============================================================

st.sidebar.title("TaxAuditAI")

st.sidebar.success("Database Connected")

st.sidebar.write("**Database:** TaxAuditAI")
st.sidebar.write("**Host:** localhost")
st.sidebar.write("**Engine:** MySQL")


# ============================================================
# TAXAUDITAI GEMINI AGENT
# ============================================================

st.header("🤖 TaxAuditAI AI Auditor")

st.write(
    "Ask questions about taxpayer audit priority, "
    "predictions, anomalies, and SHAP explanations."
)

question = st.text_area(
    "Enter your question",
    placeholder=(
        "Example: Why is taxpayer train_id887 high priority?"
    ),
    height=100
)

if st.button("Ask TaxAuditAI", type="primary"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "TaxAuditAI is analyzing the evidence..."
        ):

            try:

                answer = agent.ask_tax_auditor(
                    question.strip()
                )

                st.markdown(answer)

            except Exception as e:

                st.error(
                    "The TaxAuditAI agent could not process "
                    "the question."
                )

                st.exception(e)