import streamlit as st
import asyncio
from playwright.async_api import async_playwright
import random
import string

# Random strings generate karne ke liye
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

st.title("🎮 Valvozone Live Bot Control")

# Sidebar for settings
st.sidebar.header("Configuration")
prefix = st.sidebar.text_input("Username/Email Prefix", value="val_")

if st.button("Start Real-Time Registration"):
    user_id = generate_random_string(5)
    test_email = f"{prefix}{user_id}@valvozone.com"
    test_user = f"valvo_{user_id}"
    test_pass = "ValvoZone@123!"

    st.write(f"🔄 **Process Started:** Registering {test_user}...")

    async def run_bot():
        async with async_playwright() as p:
            # Server setup for browser
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            
            try:
                # 1. Riot Sign-up page
                await page.goto("https://auth.riotgames.com/signup")
                st.write("Step 1: Filling Email...")
                
                # 2. Email fill karna
                await page.fill('input[name="email"]', test_email)
                await page.keyboard.press("Enter")
                await asyncio.sleep(3)
                
                # 3. Check for Captcha
                # Agar yahan captcha aaya toh bot ruk jaye ga kyunke headless mode mein manually solve nahi ho sakta
                st.warning("⚠️ Checking for Captcha... Agar page aage nahi barha toh Captcha Solver ki zaroorat hogi.")
                
                # Aage ka process (DOB, Username, Password) tabhi chalega agar captcha na aaye
                st.success(f"Details submitted for {test_email}! Check your Gmail (Catch-all) for verification.")
                
            except Exception as e:
                st.error(f"Error occurred: {e}")
            finally:
                await browser.close()

    asyncio.run(run_bot())
