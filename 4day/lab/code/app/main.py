import pickle
from contextlib import asynccontextmanager

from config import LOGISTIC_MODEL, RF_MODEL
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
import asyncio 

from typing import Annotated


class IrisData(BaseModel):
    sepal_length: float = Field(
        default=1.1, gt=0, lt=10, description="Sepal length is in range (0,10)"
    )
    sepal_width: float = Field(default=3.1, gt=0, lt=10)
    petal_length: float = Field(default=2.1, gt=0, lt=10)
    petal_width: float = Field(default=4.1, gt=0, lt=10)



ml_models = {}  # Global dictionary to hold the models.


def load_model(path: str):
    model = None
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load models when the app starts
    ml_models["logistic_model"] = load_model(LOGISTIC_MODEL)
    ml_models["rf_model"] = load_model(RF_MODEL)

    yield

    # This code will be executed after the application finishes handling requests, right before the shutdown
    # Clean up the ML models and release the resources
    ml_models.clear()


# Create a FastAPI instance
app = FastAPI(lifespan=lifespan)


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/models")
async def list_models():
    print(LOGISTIC_MODEL)
    print(RF_MODEL)
    return {"available_models": list(ml_models.keys())}


@app.post("/predict/{model_name}")
async def predict(
    model_name: Annotated[str, Path(regex=r"^(logistic_model|rf_model)$")],
    iris: IrisData,
):
    # await asyncio.sleep(5) # Mimic heavy workload.

    input_data = [
        [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]
    ]

    if model_name not in ml_models.keys():
        raise HTTPException(status_code=404, detail="Model not found")

    ml_model = ml_models[model_name]
    prediction = ml_model.predict(input_data)

    return {"model": model_name, "prediction": int(prediction[0])}
