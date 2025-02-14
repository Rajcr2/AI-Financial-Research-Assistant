import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load PyTorch-based FinBERT for Financial Sentiment Analysis
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

def get_finbert_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    labels = ["negative", "neutral", "positive"]
    sentiment = labels[torch.argmax(probabilities).item()]
    return sentiment

# Function: Generate Sentiment using FinBERT
def generate_finbert_sentiment(forecast, analysis_type="long_term"):
    sentiments = []
    
    for i in range(len(forecast)):
        row = forecast.iloc[i]

        # Long-Term Sentiment
        if analysis_type == "long_term":
            text_prompt = (f"The stock is forecasted at {row['yhat']:.2f}. "
                           f"Indicators: SMA_50 = {row['SMA_50']:.2f}, RSI_21 = {row['RSI_21']:.2f}. "
                           f"Predict sentiment.")

            sentiment = get_finbert_sentiment(text_prompt)

            if sentiment == "positive":
                recommendation = "AI suggests buying this stock based on momentum."
            elif sentiment == "neutral":
                recommendation = "AI suggests holding as future movement is uncertain."
            else:
                recommendation = "AI suggests avoiding this stock for long-term."

        # sIntraday Sentiment
        else:
            quantity = int(row['Volume'] * 0.02)  

            if row['RSI_7'] > 55 and row['SMA_5'] > forecast.iloc[i-1]['SMA_5']:
                sentiment = "positive"
                recommendation = f"AI suggests buying {quantity} shares today."
            elif row['RSI_7'] < 45 and row['SMA_5'] < forecast.iloc[i-1]['SMA_5']:
                sentiment = "negative"
                recommendation = f"AI suggests selling {quantity} shares today."
            else:
                sentiment = "neutral"
                recommendation = "AI suggests holding as market conditions are stable."

        sentiments.append((row['ds'], row['yhat'], sentiment, recommendation))

    return pd.DataFrame(sentiments, columns=['Date', 'Forecast Price', 'Sentiment', 'Recommendation'])