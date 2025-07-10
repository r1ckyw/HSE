import streamlit as st

# 🚧 DEV MODE: Login is disabled for testing

st.set_page_config(page_title="HSE Dashboard", layout="wide")

st.title("Welcome 👋")
st.subheader("Health, Safety & Environment (HSE) Dashboard")

st.markdown("---")

st.markdown("""
### Navigation:
- 📊 KPIs
- 📝 Incident Reports
- 👀 Safety Observations
""")

st.info("🚨 Login is currently disabled for testing purposes.")
