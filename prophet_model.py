from prophet import Prophet

# Function: Train Prophet Model
def train_prophet(df, days):
    model = Prophet(daily_seasonality=True)
    model.fit(df)
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    return model, forecast