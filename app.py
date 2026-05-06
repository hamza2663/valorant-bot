import streamlit as st
import pandas as pd
import random
import string

# Dashboard Title
st.title("🚀 Valvozone Auto-Account Bot")

# Sidebar Configuration
st.sidebar.header("Settings")
domain = "valvozone.com" # Aapka domain
prefix = st.sidebar.text_input("Email Prefix", value="val_acc_")

# Function to generate random password
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for i in range(length))

if st.button("Generate New Account Details"):
    # Random Email generate karna
    random_id = ''.join(random.choice(string.digits) for i in range(5))
    generated_email = f"{prefix}{random_id}@{domain}"
    generated_pass = generate_password()
    
    st.success(f"Naya Account Tyar Hai!")
    
    # Display Result
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Email:** {generated_email}")
    with col2:
        st.info(f"**Password:** {generated_pass}")
    
    # Yahan hum Playwright ka code add karenge jo Riot ki site par jaye ga
    st.warning("Note: Catch-all email 'active' hona chahiye taake verification mil sake.")

# Export Option
st.download_button("Download CSV for Eldorado", data="Email,Password\nadmin@valvozone.com,Pass123", file_name="accounts.csv")
