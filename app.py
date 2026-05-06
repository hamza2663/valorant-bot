import streamlit as st
import asyncio
import os
import random
import string
from playwright.async_api import async_playwright

# --- Browser Driver Installation ---
# Ye hissa Streamlit par chromium install kare ga agar wo mojood nahi hy
def install_playwright():
    os.system("playwright install chromium")

# Helper function
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

st.title("🎮 Valvozone Live Bot Control")

# Sidebar
st.sidebar.header("Configuration")
prefix = st.sidebar.text_input("Username/Email Prefix", value="val_")

if st.button("Start Real-Time Registration"):
    # Pehle browser install karne ki koshish karein
    with st.spinner("Installing browser drivers... (Pehli baar thora waqt lag sakta hy)"):
        install_playwright()

    user_id = generate_random_string(5)
    test_email = f"{prefix}{user_id}@valvozone.com"
    test_user = f"valvo_{user_id}"
    test_pass = "ValvoZone@123!"

    st.write(f"🔄 **Process Started:** Registering {test_user}...")

    async def run_bot():
        async with async_playwright() as p:
            try:
                # Browser launch with specific arguments for Streamlit environment
                browser = await p.chromium.launch(
                    headless=True,
                    args=["--no-sandbox", "--disable-dev-shm-usage"]
                )
                context = await browser.new_context()
                page = await context.new_page()
                
                # 1. Riot Sign-up page
                st.write("Step 1: Filling Email...")
                await page.goto("https://auth.riotgames.com/signup", timeout=60000)
                
                # 2. Email fill karna
                await page.fill('input[name="email"]', test_email)
                await page.keyboard.press("Enter")
                await asyncio.sleep(5)
                
                # Check point
                st.info("Form submitted. Now checking for Captcha or next step...")
                
                # Yahan captcha handling ki zaroorat par sakti hy
                st.success(f"Details submitted for {test_email}! Check your Gmail (Catch-all) for verification.")
                
            except Exception as e:
                st.error(f"Browser Error: {e}")
            finally:
                await browser.close()

    asyncio.run(run_bot())
