# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY train_model.py . 
COPY app.py . 
COPY fraud_model.pkl . 
COPY requirements.txt . 

# Copy static files (HTML, CSS, JS, etc.)
COPY static/ static/

# Install dependencies
RUN pip install -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app with static file support
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--log-level", "info"]
