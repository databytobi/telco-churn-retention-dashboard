import streamlit as st
import pandas as pd

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Telco Churn Retention Dashboard",
    layout="wide"
)

st.title("📊 Telco Churn Retention Dashboard")
st.caption("Turning churn predictions into profitable retention decisions")

# -------------------------------
# Load Data
# -------------------------------
@st.cache_data(show_spinner=True)
def load_data():
    try:
        df = pd.read_csv("data/churn_predictions_xgb.csv")
        return df
    except FileNotFoundError:
        st.error("CSV file not found! Make sure 'data/churn_predictions_xgb.csv' exists.")
        return pd.DataFrame()  # return empty df to prevent crashes

df = load_data()

if df.empty:
    st.stop()  # Stop rendering if data is missing

# -------------------------------
# Sidebar Controls
# -------------------------------
st.sidebar.header("🔧 Decision Controls")

prob_threshold = st.sidebar.slider(
    "Churn Probability Threshold",
    min_value=0.1,
    max_value=0.9,
    value=0.6,
    step=0.05
)

# Filter high-risk customers
at_risk_df = df[df["churn_probability"] >= prob_threshold]

# -------------------------------
# KPI Metrics
# -------------------------------
st.subheader("📌 Key Metrics")

total_customers = len(df)
high_risk_customers = len(at_risk_df)
revenue_at_risk = at_risk_df["expected_loss"].sum() if not at_risk_df.empty else 0
total_net_savings = at_risk_df["net_savings"].sum() if not at_risk_df.empty else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("High-Risk Customers", f"{high_risk_customers:,}")
col3.metric("Revenue at Risk ($)", f"{revenue_at_risk:,.0f}")
col4.metric("Potential Net Savings ($)", f"{total_net_savings:,.0f}")

st.divider()

# -------------------------------
# Section 1: Revenue at Risk
# -------------------------------
st.subheader("💰 How Much Money Is at Risk?")

if not at_risk_df.empty:
    risk_by_segment = (
        at_risk_df
        .groupby("value_segment")["expected_loss"]
        .sum()
        .sort_values(ascending=False)
    )
    st.bar_chart(risk_by_segment)
    st.caption("Revenue exposure is concentrated among high-value and month-to-month customers.")
else:
    st.info("No customers exceed the current churn probability threshold.")

st.divider()

# -------------------------------
# Section 2: Who Should We Act On?
# -------------------------------
st.subheader("🎯 Who Should We Act On?")

action_df = at_risk_df[at_risk_df["net_savings"] > 0].sort_values("net_savings", ascending=False)

if not action_df.empty:
    st.dataframe(
        action_df[[
            "customerID",
            "churn_probability",
            "value_segment",
            "tenure",
            "MonthlyCharges",
            "expected_loss",
            "retention_cost",
            "net_savings",
            "action"
        ]].head(25),
        use_container_width=True
    )
    st.caption("Customers ranked by net business value — these are retention priorities.")
else:
    st.info("No customers have a positive retention ROI at this threshold.")

st.divider()

# -------------------------------
# Section 3: What Action Should We Take?
# -------------------------------
st.subheader("🛠 Retention Actions Summary")

if not action_df.empty:
    action_summary = (
        action_df
        .groupby("action")
        .agg(
            customers=("customerID", "count"),
            total_net_savings=("net_savings", "sum")
        )
        .sort_values("total_net_savings", ascending=False)
    )
    st.dataframe(action_summary, use_container_width=True)
    st.caption("Retention actions optimized for ROI, not volume.")
else:
    st.info("No retention actions recommended at this threshold.")

st.divider()

# -------------------------------
# Optional: Download Retention List
# -------------------------------
st.subheader("⬇️ Export Retention List")

if not action_df.empty:
    csv = action_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Customers to Retain (CSV)",
        data=csv,
        file_name="retention_targets.csv",
        mime="text/csv"
    )