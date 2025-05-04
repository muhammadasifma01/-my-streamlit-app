import streamlit as st
import requests

# Page title
st.set_page_config(page_title="Welcome Shoaib", page_icon="🇵🇰")
st.title("Welcome To Shoaib Afridi Website")

# Show image
st.image("images/Shoaib.jpg", caption="Welcome to Shoaib Afridi Website", use_container_width=True)

# Divider
st.markdown("---")

# Currency Exchange Rate
st.header("💱 EUR to PKR Exchange Rate")

try:
    response = requests.get("https://api.frankfurter.app/latest?from=EUR&to=PKR")
    response.raise_for_status()
    data = response.json()
    rate = data["rates"]["PKR"]
    st.success(f"💶 1 EUR = {rate:.2f} PKR 🇵🇰")
except Exception as e:
    st.error("Failed to fetch exchange rate.")
    st.exception(e)