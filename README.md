# AI based Financial Research Assistant.

## Introduction

So, In this project, I have developed a scalable AI based time-series forecasting pipeline using Prophet and BERT, designed to predict the future stock price and also Market based Sentiment  of a given company or entity specifically focusing on its performance one year ahead. The pipeline integrates critical features such as trend analysis to provide accurate and actionable forecasts and Insights.

## Objectives

The primary goal of this project is to create a AI based time-series forecasting system that can:
   1. Analyze historical data to predict future trends.
   2. Provide Investor Long-Term as well as Intraday Forecast.
   3. Based on that data to generate Market Sentiment that will provide investor a future insight.

### Prerequisites
To run this project, you need to install the following libraries:
### Required Libraries

- **Python 3.12+**
- **Yahoo Finance**: This library retrievs real-time and historical market data, stock prices.
- **Prophet**: A forecasting tool for time-series data, designed to handle trends, seasonality and holidat effects.
- **Streamlit**: Streamlit is a framework that builds interactive, data-driven web applications directly in python. 
- **PyTorch**: This library is primarily used for building and training deep learning models.
- **Transformers**: This library is given by Hugging Face as a Python package which provides pre-trained models for NLP tasks like text generation, translation, and sentiment analysis.

Other Utility Libraries : **Matplotlib**, **Pandas**, **Talib**.

### Installation

   ```
   pip install yfinance
   pip install pandas
   pip install streamlit
   pip install prophet
   pip install transformers
   pip install torch
   pip install matplotlib
   pip install ta
   ```

### Procedure

1.   Create new directory **'Financial Assistant'**.
2.   Inside that directory/folder create new environment.
   
   ```
   python -m venv financeassist
   ```

  Now, activate this **'financeassist'** venv.
  
4.   Clone this Repository :

   ```
   [https://github.com/Rajcr2/AI-Financial-Research-Assistant]
   ```
5.   Now, Install all mentioned required libraries in your environment.
6.   After, that Run **'main.py'** file from Terminal. To activate the dashboard on your browser.
   ```
   streamlit run main.py
   ``` 
7. Now, move to your browser.
8. Search Company name it will provide Entity symbol and type that symbol i.e TCS.NS. This will display all the required data.
9. then click on **'Analyze Stock'** which will provide you forecast and Real-time market sentiment.
10. Check the forecast & results and then decide whether to invest or not 😁. 



### Output

Results of MODEL :

https://github.com/user-attachments/assets/2034aeb7-99aa-475e-b697-735b4eb13f61


#### Conclusion :

The model has successfully forecasted results and provided market sentiment, helping us decide whether to invest or not. There is room for improvement in the next version, where we will feed recent news data of the given company to the LLM, enabling more accurate forecasting—stay tuned for the update!



