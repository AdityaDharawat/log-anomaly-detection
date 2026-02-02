from fastapi import FastAPI
from model.predict import detect_anomaly

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Log Anomaly Detection API running"}

@app.post("/predict")
def predict(log_level: int, response_time: int):
    result = detect_anomaly(log_level, response_time)
    return {"result": result}
