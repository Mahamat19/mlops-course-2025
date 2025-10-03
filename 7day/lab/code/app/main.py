import os
import pickle
from contextlib import asynccontextmanager
from typing import Annotated

import pandas as pd
from dotenv import load_dotenv
from evidently import Report
from evidently.presets import DataDriftPreset
from fastapi import BackgroundTasks, FastAPI, HTTPException, Path
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from sklearn.datasets import load_iris

load_dotenv()

ml_models = {}


class IrisData(BaseModel):
    sepal_length: float = Field(
        default=1.1, gt=0, lt=10, description="Sepal length is in range (0,10)"
    )
    sepal_width: float = Field(default=3.1, gt=0, lt=10)
    petal_length: float = Field(default=2.1, gt=0, lt=10)
    petal_width: float = Field(default=4.1, gt=0, lt=10)


def load_model(path: str):
    if not path:
        return None

    model = None
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["logistic_model"] = load_model(os.getenv("LOGISTIC_MODEL"))
    ml_models["rf_model"] = load_model(os.getenv("RF_MODEL"))

    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


# Create a FastAPI instance
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/models")
async def list_models():
    return {"available_models": list(ml_models.keys())}


@app.post("/predict/{model_name}")
async def predict(
    model_name: Annotated[str, Path(pattern=r"^(logistic_model|rf_model)$")],
    iris_data: IrisData,
    background_tasks: BackgroundTasks,
):
    input_data = [
        [
            iris_data.sepal_length,
            iris_data.sepal_width,
            iris_data.petal_length,
            iris_data.petal_width,
        ]
    ]

    if model_name not in ml_models.keys():
        raise HTTPException(status_code=404, detail="Model not found.")

    model = ml_models[model_name]
    prediction = model.predict(input_data)

    background_tasks.add_task(log_data, input_data[0], int(prediction[0]))

    return {"model": model_name, "prediction": int(prediction[0])}


### PART 3 solution
# Global variable for storing logs
DATA_LOG = []
DATA_WINDOW_SIZE = 45


def log_data(iris_data: list, prediction: int):
    global DATA_LOG
    iris_data.append(prediction)
    DATA_LOG.append(iris_data)


def load_train_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target
    return df


# loads our latest predictions
def load_last_predictions():
    prediction_data = pd.DataFrame(
        DATA_LOG[-DATA_WINDOW_SIZE:],
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
            "species",
        ],
    )
    return prediction_data


def generate_dashboard() -> str:
    data_report = Report(
        metrics=[
            DataDriftPreset(),
        ],
        include_tests="True",
    )

    reference_data = load_train_data()
    current_data = load_last_predictions()

    generated_report = data_report.run(
        reference_data=reference_data, current_data=current_data
    )

    return generated_report.save_html("report.html")


@app.get("/monitoring", tags=["Other"])
def monitoring():
    if len(DATA_LOG) == 0:
        return {"msg": "No data."}
    generate_dashboard()
    return FileResponse(
        path=str("report.html"),
        media_type="text/html; charset=utf-8",
        filename="monitoring_report.html",
    )
