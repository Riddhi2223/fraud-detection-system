from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Load the trained model
model = joblib.load("fraud_model.pkl")

# Mount static directory for serving HTML
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates for rendering HTML
templates = Jinja2Templates(directory="static")

# Home route to serve the HTML form
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "fraud_score": None, "decision": None})

# API route for fraud prediction
@app.post("/predict", response_class=HTMLResponse)
async def predict_fraud(
    request: Request,
    amt: float = Form(...),
    city_pop: int = Form(...),
    lat: float = Form(...),
    long: float = Form(...),
    merch_lat: float = Form(...),
    merch_long: float = Form(...)
):
    try:
        input_data = np.array([[amt, city_pop, lat, long, merch_lat, merch_long]])
        
        # Predict probability
        prediction = model.predict_proba(input_data)[0][1]
        prediction = float(prediction)

        decision = "Fraud" if prediction > 0.5 else "Not Fraud"

        return templates.TemplateResponse(
            "index.html",
            {"request": request, "fraud_score": prediction, "decision": decision}
        )

    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "fraud_score": None, "decision": f"Error: {str(e)}"}
        )
