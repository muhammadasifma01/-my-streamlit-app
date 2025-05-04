import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Real-Time Stock Market Dashboard",
    page_icon="📈",
    layout="wide"
)

# Title and description with blue font
st.markdown("<h1 style='text-align: center; color: blue;'>Welcome To Shoaib Afridi Website</h1>", unsafe_allow_html=True)

# Show the image
st.image('images/Shoaib.jpg', caption='Welcome to Shoaib Afridi Website', use_container_width=True)

# Title and description for stock market dashboard
st.title("📈 Real-Time Stock Market Dashboard")
st.markdown("""
    This dashboard provides real-time stock market data and analysis.
    Enter a stock symbol (e.g., AAPL, GOOGL, MSFT) to get started.
""")

# Sidebar for user input
st.sidebar.header("Stock Selection")
ticker = st.sidebar.text_input("Enter Stock Symbol", "AAPL").upper()

# Date range selection
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(start_date, end_date),
    min_value=end_date - timedelta(days=365*5),
    max_value=end_date
)

# Fetch stock data
@st.cache_data
def load_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    hist = stock.history(start=start_date, end=end_date)
    return hist

try:
    data = load_data(ticker, date_range[0], date_range[1])
    
    # Display basic stock info
    stock_info = yf.Ticker(ticker).info
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Current Price", f"${stock_info.get('currentPrice', 'N/A')}")
    with col2:
        st.metric("52 Week High", f"${stock_info.get('fiftyTwoWeekHigh', 'N/A')}")
    with col3:
        st.metric("52 Week Low", f"${stock_info.get('fiftyTwoWeekLow', 'N/A')}")
    
    # Create interactive candlestick chart
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    )])
    
    fig.update_layout(
        title=f"{ticker} Stock Price",
        yaxis_title="Price (USD)",
        xaxis_title="Date",
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Display additional metrics
    st.subheader("Additional Metrics")
    metrics = {
        "Market Cap": f"${stock_info.get('marketCap', 'N/A'):,.2f}",
        "P/E Ratio": stock_info.get('trailingPE', 'N/A'),
        "Volume": f"{data['Volume'].iloc[-1]:,.0f}",
        "Average Volume": f"{data['Volume'].mean():,.0f}"
    }
    
    cols = st.columns(4)
    for i, (metric, value) in enumerate(metrics.items()):
        cols[i].metric(metric, value)
    
    # Display recent news
    st.subheader("Recent News")
    news = yf.Ticker(ticker).news
    for item in news[:5]:
        st.markdown(f"""
            **{item['title']}**
            - Source: {item['publisher']}
            - Published: {datetime.fromtimestamp(item['providerPublishTime']).strftime('%Y-%m-%d %H:%M')}
            [Read more]({item['link']})
        """)
    
except Exception as e:
    st.error(f"Error loading data for {ticker}. Please check the stock symbol and try again.")
    st.error(str(e)) 