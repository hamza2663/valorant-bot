import streamlit as st
import asyncio
import os
import subprocess
from playwright.async_api import async_playwright

def install_essentials():
    # Force install only the most basic requirement via playwright directly
    st.write("Checking system dependencies...")
    try:
        # Yeh command headless browser ki basic libs install karne ki koshish karta hai
        subprocess.run(["playwright", "install-deps", "chromium"], check=True)
    except:
        st.warning("Could not auto-install deps. Trying to run anyway...")

async def run_bot_safe(email):
    playwright = await async_playwright().start()
    browser = None
    try:
        browser = await playwright.chromium.launch(
            headless=True, 
            args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"]
        )
        page = await browser.new_page()
        st.write("🌐 Opening Riot Games...")
        await page.goto("https://auth.riotgames.com/signup", timeout=60000)
        
        await page.fill('input[name="email"]', email)
        st.success(f"✅ Success! Email {email} entered.")
        
    except Exception as e:
        st.error(f"❌ Detailed Error: {e}")
    finally:
        if browser:
            await browser.close()
        await playwright.stop()

st.title("Valvozone Bot - Debug Mode")

if st.button("Run Registration"):
    with st.spinner("Setting up environment..."):
        # Step 1: Install Browser
        os.system("playwright install chromium")
        # Step 2: Try installing deps inside the container
        install_essentials()
    
    asyncio.run(run_bot_safe("test@valvozone.com"))
