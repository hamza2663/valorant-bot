import streamlit as st
import asyncio
import os
from playwright.async_api import async_playwright

async def run_bot_safe(email):
    # Playwright ko start karein
    playwright = await async_playwright().start()
    browser = None
    try:
        # Streamlit server par browser launch karne ki koshish
        browser = await playwright.chromium.launch(
            headless=True, 
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
        )
        page = await browser.new_page()
        st.write("🌍 Connecting to Riot Games...")
        await page.goto("https://auth.riotgames.com/signup", timeout=60000)
        
        await page.fill('input[name="email"]', email)
        st.success(f"✅ Success! Email {email} entered.")
        
    except Exception as e:
        st.error(f"❌ Browser Error: {e}")
    finally:
        if browser:
            await browser.close()
        await playwright.stop()

st.title("Valvozone Final Fix")

if st.button("Start Bot"):
    with st.spinner("Preparing environment..."):
        # Ye command missing libraries khud install karega
        os.system("playwright install chromium")
        os.system("playwright install-deps") 
    
    asyncio.run(run_bot_safe("test@valvozone.com"))
