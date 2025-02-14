import yfinance as yf
import ta 

# Function: Fetch Stock Data
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    df = stock.history(period="2y")
    df.reset_index(inplace=True)

    df = df[['Date', 'Open', 'Close', 'Volume']]
    
    # Ensure 'Date' column is parsed correctly
    df['Year'] = df['Date'].dt.year.astype(str)
    df['Month'] = df['Date'].dt.month.astype(str).str.zfill(2)
    df['Day'] = df['Date'].dt.day.astype(str).str.zfill(2)

    # Create 'ds' and 'y' columns for Prophet
    df['ds'] = df['Year'] + '-' + df['Month'] + '-' + df['Day']
    df['y'] = df['Close']  # Prophet's target variable

    # Drop unnecessary columns but keep 'y'
    df = df[['ds', 'y', 'Open', 'Volume']].dropna()

    return df

# Function: Compute Technical Indicators
def compute_technical_indicators(df):
    df['SMA_50'] = ta.trend.sma_indicator(df['y'], window=50)  
    df['RSI_21'] = ta.momentum.rsi(df['y'], window=21)  

    df['SMA_5'] = ta.trend.sma_indicator(df['y'], window=5)  
    df['RSI_7'] = ta.momentum.rsi(df['y'], window=7)  

    return df.dropna()
