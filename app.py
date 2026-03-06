import pickle
import pandas as pd

# Load trained model
with open("models/dengue_forecast_model.pkl", "rb") as f:
    model = pickle.load(f)

forecast = model.forecast(12)

# Remove negative predictions
forecast = forecast.clip(lower=0).round().astype(int)

print("Predicted Dengue Cases for Next 12 Months:\n")
print(forecast)