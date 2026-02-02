import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

# Load logs
df = pd.read_csv("data/logs.csv")

# Encode log level
df["log_level"] = df["log_level"].map({
    "INFO": 0,
    "WARN": 1,
    "ERROR": 2
})

X = df[["log_level", "response_time"]]

# Train Isolation Forest
model = IsolationForest(
    n_estimators=100,
    contamination=0.2,
    random_state=42
)
model.fit(X)

# Save model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved.")
