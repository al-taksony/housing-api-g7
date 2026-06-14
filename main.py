from fastapi import FastAPI
from pydantic import BaseModel

from database import engine
from models import Base
from routers import housing

app = FastAPI(
    title = "Housing API con FastAPI",
    description = "API para predecir el precio de una vivienda usando Machine Learning, FastAPI y SQLAlchemy",
    version = "1.0.0"
)

app.include_router(housing.router)

#schema
class Housing(BaseModel):
    rooms: int

@app.get("/")
def index():
    return {
        "title": "FASTAPI HOUSING API VERSION 1.0.0",
        "message": "Bienvenido a la API"
    }