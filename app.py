import streamlit as st
import asyncio
import os
import random
import string
from playwright.async_api import async_playwright

# --- Global Configurations ---
PREFIX_DEFAULT = "val_"
DOMAIN = "valvozone.com"

# --- Functions ---
def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def install_playwright():
    # Force install only if not present
    st.write("Checking browser drivers...")
    os.system("playwright install chromium")

async def run_bot(email, username, password):
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-dev-shm-usage"]
            )
            context = await browser.new_context()
            page = await context.new_page()
            
            st.info(f"Opening Riot Signup for: {username}")
            await page.goto("https://auth.riotgames.com/signup", timeout=60000)
            
            # Email Step
            await page.fill('input[name="email"]', email)
            await page.keyboard.press("Enter")
            await asyncio.sleep(5)
            
            st.success(f"Form submitted for {email}! Check your master Gmail.")
            
        except Exception as e:
            st.error(f"Execution Error: {e}")
        finally:
            await browser.close()

# --- UI ---
st.title("🎮 Valvozone Live Bot Control")

# Sidebar input defined outside any block to avoid UnboundLocalError
user_prefix = st.sidebar.text_input("Username/Email Prefix", value=PREFIX_DEFAULT)

if st.button("Start Real-Time Registration"):
    # Define variables inside the button click context
    uid = generate_random_string()
    final_email = f"{user_prefix}{uid}@{DOMAIN}"
    final_user = f"valvo_{uid}"
    final_pass = "ValvoZone@123!"

    st.write(f"🔄 **Target:** {final_user}")
    
    # Run installation
    install_playwright()
    
    # Run the bot logic
    asyncio.run(run_bot(final_email, final_user, final_pass))
