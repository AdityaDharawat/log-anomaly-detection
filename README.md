# Log Anomaly Detection using Machine Learning and DevOps

## Overview

This project implements a **log anomaly detection system** using machine learning and modern DevOps practices.
The system analyzes application or system logs to identify anomalous behavior that may indicate failures, performance degradation, or security issues.

An unsupervised machine learning model is trained to detect anomalies and is exposed as a **REST API** using FastAPI. The application is containerized with Docker and designed for cloud deployment with CI/CD support.

---

## Problem Statement

In real-world production systems, logs are generated continuously and often contain early indicators of system failures. Manually monitoring logs is inefficient and error-prone.

This project aims to:

* Automatically detect abnormal log patterns
* Provide a scalable ML-based monitoring solution
* Demonstrate DevOps best practices for ML deployment

---

## Tech Stack

### Machine Learning

* Python
* Scikit-learn
* Pandas
* NumPy
* Isolation Forest (unsupervised anomaly detection)

### Backend / API

* FastAPI
* Uvicorn

### DevOps & Deployment

* Docker
* Git
* GitHub
* Render (cloud deployment)

---

## Project Architecture

```
Logs (CSV / System Logs)
        ↓
Data Preprocessing
        ↓
Isolation Forest Model
        ↓
FastAPI Inference Service
        ↓
Docker Container
        ↓
Cloud Deployment (Render)
```

---

## Folder Structure

```
log-anomaly-detection/
│
├── data/
│   └── logs.csv
│
├── model/
│   ├── train.py
│   ├── predict.py
│   └── model.pkl
│
├── app/
│   └── main.py
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Machine Learning Approach

### Model Used

**Isolation Forest**

### Reason for Selection

* Works well with high-volume log data
* Does not require labeled anomaly data
* Efficient for real-time anomaly detection
* Commonly used in monitoring and security systems

### Features Used

* Log level (encoded as numeric values)
* Response time (latency)

---

## API Endpoints

### Root Endpoint

**GET /**

```json
{
  "status": "Log Anomaly Detection API running"
}
```

### Anomaly Prediction

**POST /predict**

**Request Parameters**

```json
{
  "log_level": 2,
  "response_time": 900
}
```

**Response**

```json
{
  "result": "Anomaly"
}
```

---

## Running the Project Locally

### Prerequisites

* Python 3.9+
* pip
* Docker (optional for containerized execution)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python model/train.py
```

### Run the API

```bash
python -m uvicorn app.main:app --reload
```

Access the API documentation at:

```
http://127.0.0.1:8000/docs
```

---

## Running with Docker

### Build Docker Image

```bash
docker build -t log-anomaly .
```

### Run Container

```bash
docker run -p 8000:8000 log-anomaly
```

The API will be available at:

```
http://localhost:8000
```

---

## DevOps Concepts Demonstrated

* Log-based monitoring
* ML model deployment as a microservice
* Containerization using Docker
* Version control using Git and GitHub
* Cloud deployment with automated builds
* Reproducible and portable ML pipelines

---

## Deployment

The application is designed to be deployed on cloud platforms such as **Render** using Docker.
Each push to GitHub can automatically trigger a new build and deployment.

---

## Future Enhancements

* Real-time log ingestion
* Integration with databases (MongoDB / PostgreSQL)
* Streamlit-based monitoring dashboard
* CI/CD pipeline using GitHub Actions
* Alerting system for detected anomalies
* Support for real server logs (Apache / Nginx)
