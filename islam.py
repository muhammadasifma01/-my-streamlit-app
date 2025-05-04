import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Welcome Shoaib", layout="centered")

# Title
st.title("Welcome To Shoaib Afridi Website")

# Show image
st.image("images/Shoaib.jpg", caption="Welcome to Shoaib Afridi Website", use_container_width=True)

# Divider
st.markdown("---")

# Exchange rate section
st.subheader("💱 EUR to PKR Exchange Rate")

try:
    # Use exchangerate.host API which supports PKR
    response = requests.get("https://api.exchangerate.host/latest?base=EUR&symbols=PKR")
    response.raise_for_status()
    data = response.json()
    rate = data["rates"]["PKR"]
    st.success(f"1 EUR = {rate:.2f} PKR")
except requests.exceptions.RequestException as e:
    st.error("Failed to fetch exchange rate.")
    st.exception(e)