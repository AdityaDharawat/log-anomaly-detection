import pickle
import pandas as pd

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

def detect_anomaly(log_level, response_time):
    df = pd.DataFrame([[log_level, response_time]],
                      columns=["log_level", "response_time"])
    prediction = model.predict(df)
    return "Anomaly" if prediction[0] == -1 else "Normal"
