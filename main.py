from yahooquery import search
import streamlit as st
import pandas as pd
from data_loader import get_stock_data, compute_technical_indicators
from prophet_model import train_prophet
from llm_sentiment import generate_finbert_sentiment

# Set Streamlit page configuration
st.set_page_config(page_title="AI Financial Research Assistant", layout="wide")

# Section 1: Yahoo Query to Search for Ticker Symbol
st.sidebar.title("Find Stock Symbol")
company_name = st.sidebar.text_input("Enter Company Name", "")

if st.sidebar.button("Search Symbol"):
    if company_name.strip():
        results = search(company_name)
        if "name" in results and results["name"]:
            st.sidebar.write("### Matching Stocks:")
        else:
            st.sidebar.warning("No results found. Try a different name.")
    else:
        st.sidebar.warning("Please enter a company name.")

# Section 2: Stock Analysis & Forecasting
st.title("AI Financial Research Assistant")

stock_symbol = st.text_input("Enter Stock Symbol (e.g., TCS.NS, RELIANCE.NS)", "TCS.NS")
forecast_days = st.slider("Select Forecast Days", 7, 365, 30)

if st.button("Analyze Stock"):
    try:
        # Step 1: Fetch and Process Stock Data
        stock_data = get_stock_data(stock_symbol)
        stock_data = compute_technical_indicators(stock_data)
        st.write("### Stock Data Preview", stock_data.tail())

        stock_data['ds'] = pd.to_datetime(stock_data['ds'])

        # 🔵 **Long-Term Forecast**
        st.subheader("Long-Term Investment Forecast")
        model_long, forecast_long = train_prophet(stock_data[['ds', 'y']], forecast_days)
        forecast_long = forecast_long.merge(stock_data[['ds', 'y', 'SMA_50', 'RSI_21']], on='ds', how='left')

        # Generate Sentiment for Long-Term
        sentiment_long = generate_finbert_sentiment(forecast_long, "long_term")
        st.write("### AI-Powered Long-Term Sentiments", sentiment_long.tail())

        # Plot Long-Term Forecast
        st.pyplot(model_long.plot(forecast_long))
        st.pyplot(model_long.plot_components(forecast_long))

        # **Intraday Forecast**
        st.subheader("Intraday Trading Analysis")
        intraday_data = stock_data[['ds', 'Open', 'Volume']].dropna()
        intraday_data = intraday_data.rename(columns={'Volume': 'y'})

        model_intraday, forecast_intraday = train_prophet(intraday_data, forecast_days)

        # Fix: Drop NaNs before merging & backfill missing values
        intraday_features = stock_data[['ds', 'Open', 'Volume', 'SMA_5', 'RSI_7']].dropna()
        forecast_intraday = forecast_intraday.merge(intraday_features, on='ds', how='left')
        forecast_intraday.fillna(method='ffill', inplace=True)  # Fix NaN issue

        # Generate Sentiment for Intraday
        sentiment_intraday = generate_finbert_sentiment(forecast_intraday, "intraday")
        st.write("### AI-Powered Intraday Sentiments", sentiment_intraday.tail())

        # Plot Intraday Forecast
        st.pyplot(model_intraday.plot(forecast_intraday))
        st.pyplot(model_intraday.plot_components(forecast_intraday))

    except Exception as e:
        st.error(f"Error: {e}")
