import streamlit as st
import asyncio
import os
import random
import string
from playwright.async_api import async_playwright

# --- Functions ---
def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def install_playwright():
    st.write("Checking browser drivers...")
    os.system("playwright install chromium")

async def run_bot(email, username, password):
    async with async_playwright() as p:
        browser = None # Pehle se define kar diya taake error na aaye
        try:
            browser = await p.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-dev-shm-usage"]
            )
            context = await browser.new_context()
            page = await context.new_page()
            
            st.info(f"Opening Riot Signup...")
            await page.goto("https://auth.riotgames.com/signup", timeout=60000)
            
            await page.fill('input[name="email"]', email)
            await page.keyboard.press("Enter")
            await asyncio.sleep(5)
            
            st.success(f"Form submitted for {email}!")
            
        except Exception as e:
            st.error(f"Execution Error: {e}")
        finally:
            if browser: # Sirf tab close karein agar browser define hua ho
                await browser.close()

# --- UI ---
st.title("🎮 Valvozone Live Bot Control")
user_prefix = st.sidebar.text_input("Prefix", value="val_")

if st.button("Start Registration"):
    uid = generate_random_string()
    final_email = f"{user_prefix}{uid}@valvozone.com"
    
    install_playwright()
    asyncio.run(run_bot(final_email, f"valvo_{uid}", "ValvoZone@123!"))
