from fastapi import FastAPI
from app.models import load_model
from app.schema import EmpTerm
import pandas as pd

app = FastAPI()

model = load_model()


@app.get("/")
def home():
    return {"message": "Welcome to Fast API API"}


@app.get("/")
def api_test():
    return {"message": "This fucntion is to test Api"}


@app.post("/predict-termination")
def predict_termination(data: EmpTerm):
    input_data = pd.DataFrame([
        data.dict()
    ]
    )

    prediction = model.predict(input_data)[0]
    return {
        "predicted Termination": int(prediction),
        "Status": "Terminated" if prediction == 1 else "Active"
    }
