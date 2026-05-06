import streamlit as st
import asyncio
import os
from playwright.async_api import async_playwright

async def run_bot_safe(email):
    # Browser ko start mein hi define kar diya
    playwright = await async_playwright().start()
    browser = None
    try:
        st.write("Launching browser...")
        browser = await playwright.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        await page.goto("https://auth.riotgames.com/signup")
        await page.fill('input[name="email"]', email)
        st.success(f"Email entered for {email}")
    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        if browser:
            await browser.close()
        await playwright.stop()

st.title("Valvozone Final Fix")
if st.button("Test Registration"):
    os.system("playwright install chromium")
    asyncio.run(run_bot_safe("test@valvozone.com"))
