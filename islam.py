import streamlit as st
import random
import requests
from PIL import Image, ImageOps
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Welcome Shoaib", layout="centered")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a feature", [
    "Home",
    "Inspirational Quote Generator",
    "Weather App",
    "Poll",
    "Image Filter",
    "Time-Based Greeting",
    "Cryptocurrency Prices",
    "Random Joke Generator"
])

# Home page
if page == "Home":
    st.title("Welcome To Shoaib Afridi Website")
    st.image("images/Shoaib.jpg", caption="Welcome to Shoaib Afridi Website", use_container_width=True)

# Inspirational Quote Generator
elif page == "Inspirational Quote Generator":
    st.title("💬 Inspirational Quote")
    quotes = [
        "The best way to predict the future is to create it.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "The only way to do great work is to love what you do.",
        "Believe you can and you're halfway there.",
        "Do not wait to strike till the iron is hot, but make it hot by striking."
    ]
    quote = random.choice(quotes)
    st.write(f"**{quote}**")

# Weather App
elif page == "Weather App":
    st.title("🌦️ Weather App")
    city = st.text_input("Enter the city name:", "London")
    api_key = "YOUR_API_KEY"  # Get it from https://openweathermap.org/api
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]
        st.write(f"**Weather in {city}:**")
        st.write(f"Temperature: {main_data['temp'] - 273.15:.2f}°C")
        st.write(f"Weather: {weather_data['description'].capitalize()}")
    else:
        st.write("City not found. Please try again.")

# Poll
elif page == "Poll":
    st.title("🗳️ Poll")
    poll_question = "What's your favorite programming language?"
    options = ["Python", "JavaScript", "C++", "Java", "Rust"]
    selected_option = st.radio(poll_question, options)
    if selected_option:
        st.write(f"You selected: {selected_option}")

# Image Filter
elif page == "Image Filter":
    st.title("🎨 Image Filter")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Apply Black & White Filter"):
            bw_image = image.convert("L")
            st.image(bw_image, caption="Black & White Image", use_container_width=True)

        if st.button("Apply Sepia Filter"):
            sepia_image = ImageOps.colorize(image.convert("L"), '#704214', '#C0C0C0')
            st.image(sepia_image, caption="Sepia Image", use_container_width=True)

# Time-Based Greeting
elif page == "Time-Based Greeting":
    st.title("⏰ Time-Based Greeting")
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
    elif current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    st.write(f"**{greeting}, Shoaib!** Welcome to the website!")

# Cryptocurrency Prices
elif page == "Cryptocurrency Prices":
    st.title("💸 Cryptocurrency Prices")
    cryptos = ['bitcoin', 'ethereum', 'ripple']
    prices = {}

    for crypto in cryptos:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        prices[crypto] = data[crypto]['usd']

    for crypto, price in prices.items():
        st.write(f"{crypto.capitalize()}: ${price:.2f}")

# Random Joke Generator
elif page == "Random Joke Generator":
    st.title("😂 Random Joke Generator")
    if st.button("Get a Random Joke"):
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()
        st.write(f"**{data['setup']}**")
        st.write(f"**{data['punchline']}**")