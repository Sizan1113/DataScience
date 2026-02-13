from fastapi import FastAPI
from models import load_model
from schema import EmpTerm

app = FastAPI()

model = load_model()


@app.get("/")
def home():
    return {"message": "Welcome to Fast API API"}
