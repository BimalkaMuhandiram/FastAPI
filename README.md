
# FastAPI Car Recommender Application

This repository contains a FastAPI-based machine learning application for predicting car types. The application uses a Decision Tree Classifier model to recommend car types based on input features such as age and gender.

---

## Project Overview

The **Car Recommender** application predicts a car type based on user input using machine learning. It provides REST API endpoints to interact with the model and supports seamless deployment on Heroku.

## Features

- **Prediction Endpoint**: Accepts `age` and `gender` as input and predicts the car type.
- **Swagger Documentation**: Interactive documentation available for testing API endpoints.
- **FastAPI Framework**: Lightweight, asynchronous Python framework.
- **Heroku Deployment**: Easily deployable to Heroku with CI/CD support.

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BimalkaMuhandiram/FastAPI.git
   cd YourRepository
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then, install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the Model**:
   Run the `model_1.py` file to train the Decision Tree model and save it as `car-recommender.joblib`:
   ```bash
   python model_1.py
   ```

4. **Run the Application**:
   Start the FastAPI application locally:
   ```bash
   uvicorn app:app --reload
   ```
   Visit `http://127.0.0.1:8000/docs` to see the API documentation.

---

## Deployment on Heroku

1. **Create a Heroku App**:
   - Log in to [Heroku](https://heroku.com) and create a new app.

2. **Set Up the Project**:
   - Make sure the repository has a `Procfile` for deployment:
     ```
     web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
     ```

3. **Push to Heroku**:
   Deploy the app to Heroku using the CLI:
   ```bash
   git push heroku main
   ```

4. **CI/CD Pipeline**:
   - Configure Heroku pipelines for automatic deployment from GitHub.

5. **Access Your App**:
   - Visit the app's URL to access the deployed API and its Swagger UI (`/docs`).

---

## API Documentation

The application provides interactive API documentation using Swagger UI. Here's how to interact with the API:

### Endpoints:

1. **Root Endpoint**:
   - URL: `/`
   - Method: GET
   - Response: `{"message": "Cars Recommender ML API Text"}`

2. **Prediction Endpoint**:
   - URL: `/car/predict`
   - Method: POST
   - Input: JSON body with `age` (int) and `gender` (int).
   - Example:
     ```json
     {
       "age": 25,
       "gender": 1
     }
     ```
   - Response: Predicted car type.

---

## Files in the Repository

1. **`app.py`**:
   Main FastAPI application for handling API endpoints.

2. **`CarUser.py`**:
   Pydantic model defining the structure of the input data.

3. **`model_1.py`**:
   Script to train the Decision Tree Classifier and save the model.

4. **`requirements.txt`**:
   Contains all Python dependencies for the project.

5. **`Procfile`**:
   Defines how the application runs on Heroku.

6. **`cars.csv`**:
   Dataset used for training the machine learning model.

7. **`car-recommender.joblib`**:
   Trained and serialized machine learning model.

8. **`main.py`**:
   Alternative entry point for the FastAPI application.

---

## Technologies Used

- **Python**: Programming language.
- **FastAPI**: Framework for building APIs.
- **Scikit-learn**: Machine learning library.
- **Joblib**: Model serialization.
- **Heroku**: Deployment platform.
- **Swagger UI**: Interactive API documentation.

---

## Deployment Screenshots

### 1. Heroku CI/CD Pipeline
![Heroku Pipeline](./Capture26.JPG)

### 2. Swagger UI
![Swagger UI](./Capture27.JPG)

---

## Contributing

Feel free to fork this repository and submit pull requests for enhancements or bug fixes.

---

## License

This project is licensed under the MIT License.
