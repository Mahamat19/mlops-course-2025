import pickle
from contextlib import asynccontextmanager

from config import LOGISTIC_MODEL, RF_MODEL
from fastapi import FastAPI

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
