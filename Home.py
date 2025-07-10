import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load config from users.yaml
with open('users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize authenticator
authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie_name=config['cookie']['name'],
    key=config['cookie']['key'],
    expiry_days=config['cookie']['expiry_days']
)

# Show login widget
authenticator.login()

# If user is authenticated
if st.session_state["authentication_status"]:
    authenticator.logout("Logout", "sidebar")
    st.title(f"Welcome, {st.session_state['name']} 👋")
    st.markdown("## Health, Safety & Environment (HSE) Dashboard")
    st.info("Use the sidebar to navigate.")

# If user is not authenticated
elif st.session_state["authentication_status"] is False:
    st.error("❌ Incorrect username or password")

# If user has not attempted login yet
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your credentials 👇")
