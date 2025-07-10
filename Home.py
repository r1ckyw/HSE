import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load users.yaml
with open('users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.title(f"Welcome, {name} 👋")
    st.subheader("Health, Safety & Environment (HSE) Dashboard")

    st.markdown("""
    Use the sidebar to navigate to:
    - **KPI tracking**
    - **Incident reports**
    - **Safety observations**
    """)

elif authentication_status is False:
    st.error('Username/password is incorrect ❌')
elif authentication_status is None:
    st.warning('Please enter your credentials 👇')
