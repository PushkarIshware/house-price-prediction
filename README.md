# 🏠 House Price Prediction using Machine Learning

A Machine learning model to predict house price per unit area based on features like location, age, nearby convenience store count, etc. The model is served via a REST API using FastAPI and is containerized with Docker for scalable deployment.

## 📌 Overview

This project aims to build, evaluate, and deploy a regression model that predicts housing prices based on key features such as:

- House age
- Distance to MRT station
- Number of nearby convenience stores
- Geographic coordinates
- Transaction date
- Year
- Month
- Day

## 🚀 Features

- Machine learning model using scikit-learn
- REST API with FastAPI
- Swagger UI for testing
- Dockerized deployment

## 📂 Dataset

- **Source**: [Kaggle - Real Estate Price Prediction Dataset](https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction)

## 🤖 Model Used

The following models were trained:

- Linear Regression
- Lasso Regression
- Random Forest
- Decision Tree

## 🧰 Requirements

- Python 3.9+
- pip3
- Docker

## 🗂️ Directory Structure

```
house-price-prediction/
├── ai_model/
│   ├── RF_model.pkl
│   └── RF_scaler.pkl
|
├── app/
│   ├── main.py
|
├── notebooks/
│   └── main.ipynb
│
├── raw_data/
│   └── real_estate.csv
│
├── Dockerfile
├── requirements.txt
├── presentation.pptx
└── README.md

```

## 📦 Installation (Local)

1. Clone the repository:
   ```bash
   git clone https://github.com/PushkarIshware/house-price-prediction.git
   cd house-price-prediction
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```

## 🐳 Run with Docker

To build and run the app using Docker:

```bash
docker build -t house-price-prediction .
docker run -p 8000:8000 house-price-prediction
```


## 🌐 FastAPI Endpoint

### Swagger UI: 
[http:localhost:8000/docs](http:localhost:8000/docs)

### Predict API Endpoint:

[http://localhost:8000/docs#/Predict/predict_price_predict_post](http://localhost:8000/docs#/Predict/predict_price_predict_post)

### `/predict` API:

#### Sample Request (JSON)
```json
{
  "house_age": 15.0,
  "distance_to_mrt": 250.0,
  "num_convenience_stores": 5,
  "latitude": 24.982,
  "longitude": 121.543,
  "year": 2000,
  "month": 1,
  "day": 1
}
```

#### Sample Response (JSON)
```json
{
  "predicted_price_per_unit_area": 51.7
}
```

## ✅ Conclusion
This project shows how to use machine learning to predict house prices, from data analysis and model training to making predictions through an API using FastAPI and Docker.