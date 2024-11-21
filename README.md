# 🚗 FastAPI Car Recommender Application

This repository contains a FastAPI-based machine learning application for recommending car types. The application uses a **Decision Tree Classifier** model to predict car types based on user input features such as **age** and **gender**.

---

## 🛠️ Project Overview

The **Car Recommender** application predicts car types based on user inputs (e.g., age and gender) using a trained machine learning model. It provides REST API endpoints to interact with the model and can be easily deployed using **Google Cloud Run**. The project also integrates with **CI/CD pipelines** using **GitHub Actions** for automatic deployment.

---

## ✨ Features

- **Prediction Endpoint**: Accepts `age` and `gender` as input and predicts the car type.
- **Swagger Documentation**: Interactive API documentation for testing API endpoints.
- **FastAPI Framework**: Lightweight, asynchronous Python framework.
- **Google Cloud Run Deployment**: Easily deployable to Google Cloud Run.
- **CI/CD Pipeline**: Automated build, test, and deployment via GitHub Actions.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository:
```bash
git clone https://github.com/BimalkaMuhandiram/FastAPI.git
cd FastAPI
```

### 2. Install Dependencies:
Make sure you have Python installed, then install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Train the Model:
To train the Decision Tree model and save it as `car-recommender.joblib`, run:
```bash
python model_1.py
```

### 4. Run the Application Locally:
Start the FastAPI application locally with Uvicorn:
```bash
uvicorn app:app --reload
```
Visit the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the endpoints.

---

## ☁️ Deployment on Google Cloud Run

This application is deployed on Google Cloud Run, ensuring scalability and easy deployment. Here's how you can set up the deployment:

### 1. Build and Push Docker Image:
Ensure you have Docker installed and that you are logged in to Google Cloud:
```bash
gcloud auth configure-docker
```

Build and push the Docker image to Google Container Registry (GCR):
```bash
docker build -t gcr.io/your-project-id/fastapi-car-recommender .
docker push gcr.io/your-project-id/fastapi-car-recommender
```

### 2. Deploy to Google Cloud Run:
Deploy the Docker image to Cloud Run:
```bash
gcloud run deploy fastapi-car-recommender   --image gcr.io/your-project-id/fastapi-car-recommender   --platform managed   --region us-central1   --allow-unauthenticated
```

### 3. Access the Deployed Application:
After the deployment completes, visit the provided URL (e.g., `https://fastapi-car-recommender-<random>.run.app`) to access the live application.

---

## 🔄 CI/CD Pipeline (GitHub Actions)

The project includes a CI/CD pipeline using GitHub Actions for automatic testing and deployment. The pipeline is triggered on push to the main branch, and it performs the following steps:

- **Build**: Builds the Docker image.
- **Test**: Runs the unit tests for the application.
- **Deploy**: Pushes the Docker image to Google Container Registry and deploys it to Google Cloud Run.

### 🧪 How to Test the CI/CD Pipeline:
1. Make a change in the repository (e.g., update a file).
2. Push the changes to the main branch:
   ```bash
   git add .
   git commit -m "Test CI/CD pipeline"
   git push origin main
   ```

Monitor the GitHub Actions workflow on the **Actions** tab of your GitHub repository to ensure the pipeline completes successfully.

---

## 📄 API Documentation

The application provides interactive API documentation using Swagger UI. Here's how to interact with the API:

### Endpoints:

#### Root Endpoint:
- **URL**: `/`
- **Method**: `GET`
- **Response**:
   ```json
   {
     "message": "Cars Recommender ML API"
   }
   ```

#### Prediction Endpoint:
- **URL**: `/car/predict`
- **Method**: `POST`
- **Input**: JSON body with `age` (int) and `gender` (int).
- **Example**:
   ```json
   {
     "age": 25,
     "gender": 1
   }
   ```
- **Response**: Predicted car type.

---

## 📁 Files in the Repository

- `app.py`: Main FastAPI application for handling API endpoints.
- `CarUser.py`: Pydantic model defining the structure of the input data.
- `model_1.py`: Script to train the Decision Tree Classifier and save the model.
- `requirements.txt`: Contains all Python dependencies for the project.
- `Procfile`: Defines how the application runs on Heroku (if applicable).
- `cars.csv`: Dataset used for training the machine learning model.
- `car-recommender.joblib`: Trained and serialized machine learning model.
- `main.py`: Alternative entry point for the FastAPI application.
- `.github/workflows/ci-cd.yml`: GitHub Actions workflow for CI/CD pipeline.

---

## 🔧 Technologies Used

- **Python**: Programming language.
- **FastAPI**: Framework for building APIs.
- **Scikit-learn**: Machine learning library.
- **Joblib**: Model serialization.
- **Google Cloud Run**: Deployment platform.
- **GitHub Actions**: CI/CD pipeline for automated deployment.
- **Docker**: Containerization platform.
- **Swagger UI**: Interactive API documentation.

---

## 🛠️ Troubleshooting

### Deployment Failures:
- Ensure that the Docker image is built successfully and pushed to Google Container Registry.
- Check the Cloud Run logs for errors related to container start or service initialization.
### CI/CD Pipeline Errors:
- Check the logs in GitHub Actions to identify any issues in the build, test, or deploy steps.
- Verify that all secrets (e.g., `GCP_CREDENTIALS_JSON`) are correctly set in the GitHub repository's Secrets settings.

### Model Not Loading:
- Ensure the `car-recommender.joblib` file is in the correct directory and accessible by the FastAPI application.
