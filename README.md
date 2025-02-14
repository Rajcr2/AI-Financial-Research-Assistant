# AI based Financial Research Assistant.

## Introduction

This is the Next Version of my Prophet based Stock Forecasting (https://github.com/Rajcr2/Prophet-Forecasting) Project. 
So, In this project, I have developed a scalable AI based time-series forecasting pipeline using Prophet and BERT, designed to predict the future stock price and also Market based Sentiment  of a given company or entity specifically focusing on its performance one year ahead. The pipeline integrates critical features such as trend analysis to provide accurate and actionable forecasts and Insights.

## Objectives

The primary goal of this project is to create a AI based time-series forecasting system that can:
   1. Analyze historical data to predict future trends.
   2. Based on that data to generate Market Sentiment that will provide investor a future insight.

### Prerequisites
To run this project, you need to install the following libraries:
### Required Libraries

- **Python 3.12+**
- **Yahoo Finance**: This library performs data manipulation and analysis also provides powerful data structures like dataframes.
- **Prophet**: A forecasting tool for time-series data, designed to handle trends, seasonality and holidat effects.
- **Streamlit**: Streamlit is a framework that builds interactive, data-driven web applications directly in python. 
- **PyTorch**: An Open-source platform for tracking, managing and deploying machine learning workflows.

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
   https://github.com/Rajcr2/Prophet-Forecasting.git
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

https://github.com/user-attachments/assets/e63e357a-aae7-4dc9-8bf5-4e07b7928a27






#### Entities Forecast By MODEL :
#### 1. USD-INR 
Model has predicted INR has expected to maintain stability against USD by end of 2025, showing minimal fluctuations in its exchange rate indicating a stable currency.

![USD_INR](https://github.com/user-attachments/assets/888429bb-6b05-4d17-9eca-432b33c1441d)


#### 2. TCS

As per Model, TCS Stock is projected to experience a 1.58% change by the end of 2025, indicating slight growth or decline which reflecting steady market trend for company.

![TCS_crp](https://github.com/user-attachments/assets/9e1a7139-670d-4993-9581-30bbd3932124)

#### 3. INFOSYS

Infosys stock is expected to undergo an 7.72% change by end of 2025, reflecting a moderate but significant movement in the company's market performance over the period.

![infosys_latest](https://github.com/user-attachments/assets/3554f6e6-238e-414c-9336-104e778b6fa1)


