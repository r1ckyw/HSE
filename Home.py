import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load config from users.yaml
with open('users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize the authenticator (no preauthorized field needed anymore)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Show login form in main content area
name, authentication_status, username = authenticator.login('Login', location='main')

# After login
if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.title(f"Welcome, {name} 👋")
    st.markdown("---")
    st.subheader("Health, Safety & Environment (HSE) Dashboard")

    st.markdown("""
    ### Navigate Using Sidebar:
    - 📊 KPIs
    - 📝 Incident Reports
    - 👀 Safety Observations
    """)

# If login fails
elif authentication_status is False:
    st.error("❌ Incorrect username or password")

# If no login attempt yet
elif authentication_status is None:
    st.warning("Please enter your credentials 👇")
