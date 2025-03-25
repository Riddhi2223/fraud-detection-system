# Fraud Detection System

Access the Fraud Detection System at: https://frauddetectionapiv1.whiteglacier-3a93264f.westus2.azurecontainerapps.io.
Note: I'm using a lower-power CPU for cost optimization, so please allow some time for the system to load on the first request.

## Overview
The **Fraud Detection System** is a machine-learning-powered application that predicts fraudulent transactions in real-time. The system utilizes **XGBoost** for fraud classification, **FastAPI** as a web service, **Docker** for containerization, and is deployed on **Microsoft Azure Container Apps** for scalability and reliability.

---

## Features
**Real-time Fraud Prediction** – Input transaction details and get instant fraud probability.  
**Machine Learning Model** – Uses **XGBoost** for high accuracy.  
**FastAPI Backend** – Low latency and efficient API service.  
**Web Interface** – Simple and professional UI for user interaction.  
**Containerized Deployment** – Packaged with **Docker** for easy deployment.  
**Azure Cloud Hosting** – Scalable deployment using **Azure Container Apps**.  

---

## Project Structure
```
fraud_detection_app/
│── static/                   # Static files (HTML, CSS)
│   ├── index.html
│── fraud_model.pkl            # Trained XGBoost model
│── train_model.py             # Model training script
│── app.py                     # FastAPI web service
│── requirements.txt           # Dependencies
│── Dockerfile                 # Docker container setup
│── README.md                  # Documentation
```

---

## Setup & Installation

### 1️. Clone the Repository
```sh
git clone https://github.com/Riddhi2223/fraud-detection-system.git
cd fraud-detection
```

### 2️. Install Dependencies
Make sure you have Python 3.9+ installed. Then install the required libraries:  
```sh
pip install -r requirements.txt
```

### 3️. Train the Model (Optional)
If you need to retrain the model, run:
```sh
python train_model.py
```
If you want to retrain the model, please download the dataset from the following link:
https://www.kaggle.com/datasets/kartik2112/fraud-detection/data?select=fraudTrain.csv

Once downloaded, you can use it to retrain the model as per your needs.

This will generate a new `fraud_model.pkl` file.

### 4️. Run the FastAPI Application
```sh
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
The API will be accessible at `http://localhost:8000`.

### 5️. Access the Web Interface  
Open `http://localhost:8000/` in your browser to use the fraud detection form.

---

## Docker Deployment

### 1️. Build the Docker Image  
```sh
docker build -t fraud-detection-api .
```

### 2️. Run the Docker Container  
```sh
docker run -p 8000:8000 fraud-detection-api
```
The app will be available at `http://localhost:8000/`.

---

## Azure Deployment

### 1️. Login to Azure
```sh
az login
```

### 2️. Create Azure Container Registry (ACR)
```sh
az acr create --resource-group myResourceGroup --name myRegistry --sku Basic
az acr login --name myRegistry
```

### 3️. Build & Push the Docker Image
```sh
docker tag fraud-detection-api myRegistry.azurecr.io/fraud-detection-api:latest
docker push myRegistry.azurecr.io/fraud-detection-api:latest
```

### 4️. Deploy to Azure Container Apps
```sh
az containerapp create --name fraud-api --resource-group myResourceGroup \
  --image myRegistry.azurecr.io/fraud-detection-api:latest \
  --target-port 8000 --ingress external
```
The API will be accessible via the Azure-generated URL.

---

## Usage
1. **Enter transaction details** (amount, location, etc.) on the web form.  
2. **Submit the form** to analyze the transaction.  
3. **Get the fraud probability** and classification result (`Fraud` or `Not Fraud`).  

---

## Future Enhancements
**Database Integration** – Store transaction logs in Azure SQL or CosmosDB.  
**User Authentication** – Implement OAuth for secure API access.  
**Advanced Models** – Experiment with deep learning for improved accuracy.  
**Logging & Monitoring** – Use Azure Application Insights for tracking.  

