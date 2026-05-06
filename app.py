import streamlit as st
import asyncio
import os
from playwright.async_api import async_playwright

async def run_bot_safe(email):
    playwright = await async_playwright().start()
    browser = None
    try:
        # Streamlit server par chromium launch
        browser = await playwright.chromium.launch(
            headless=True, 
            args=["--no-sandbox", "--disable-gpu"]
        )
        page = await browser.new_page()
        st.write("🌐 Opening Riot Games...")
        await page.goto("https://auth.riotgames.com/signup", timeout=60000)
        
        await page.fill('input[name="email"]', email)
        st.success(f"✅ Success! Email {email} entered.")
        
    except Exception as e:
        st.error(f"❌ Browser Error: {e}")
    finally:
        if browser:
            await browser.close()
        await playwright.stop()

st.title("Valvozone Bot - Final Test")

if st.button("Run Registration"):
    # Pehle check karein ke chromium folder mojood hy ya nahi
    if not os.path.exists("/home/appuser/.cache/ms-playwright/chromium-1112"): 
        with st.spinner("Setting up browser..."):
            os.system("playwright install chromium")
    
    asyncio.run(run_bot_safe("test@valvozone.com"))
