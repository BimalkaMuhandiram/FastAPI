# FastAPI Car Recommender

This project is a machine learning-based car recommender application built using **FastAPI**. It predicts car types based on user input (age and gender) using a trained decision tree model. The app is deployed on **Heroku** with an API endpoint and Swagger documentation for easy testing.

---

## Features

- **Machine Learning Model**: Uses a Decision Tree Classifier to predict car types.
- **FastAPI Framework**: Provides a high-performance, easy-to-use web API.
- **Interactive API Documentation**: Automatically generated Swagger UI for testing endpoints.
- **Deployed on Heroku**: Accessible as a live web application.

---

## Files Overview

### 1. `CarUser.py`
Defines the Pydantic model `CarUser` for input data validation. It includes:
- `age` (integer)
- `gender` (integer)

### 2. `model_1.py`
- Loads the `cars.csv` dataset.
- Trains a **Decision Tree Classifier** on the data.
- Persists the trained model as `car-recommender.joblib`.

### 3. `app.py`
The core FastAPI application:
- Loads the trained model.
- Exposes two endpoints:
  - `/`: A welcome message.
  - `/car/predict`: Accepts JSON input (`age` and `gender`) and predicts the car type.

### 4. `main.py`
Alternate API file showcasing another endpoint:
- `/predict`: Accepts two features (`feature_1`, `feature_2`) and predicts car types.

### 5. `Procfile`
Specifies the Heroku configuration to run the app with Gunicorn:
```plaintext
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
