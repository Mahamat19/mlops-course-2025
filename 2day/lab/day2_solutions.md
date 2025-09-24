# Lab Solutions: Experiment Tracking with MLflow

## Table of Contents

- [Lab Solutions: Experiment Tracking with MLflow](#lab-solutions-experiment-tracking-with-mlflow)
  - [Table of Contents](#table-of-contents)
  - [Theory Overview](#theory-overview)
  - [Part 1: Getting Started with MLflow](#part-1-getting-started-with-mlflow)
    - [Task 1: Install and run MLflow UI](#task-1-install-and-run-mlflow-ui)
    - [Task 2: Autologging](#task-2-autologging)
  - [Part 2: Manual Logging and Experiment Management](#part-2-manual-logging-and-experiment-management)
    - [Task 1: Log parameters, metrics, tags and the model manually](#task-1-log-parameters-metrics-tags-and-the-model-manually)
    - [Task 2: Compare runs in the UI](#task-2-compare-runs-in-the-ui)
  - [Part 3: Working with Artifacts](#part-3-working-with-artifacts)
    - [Task 1: Save artifacts (plots, preprocessing objects)](#task-1-save-artifacts-plots-preprocessing-objects)
    - [Task 2: Log and reload a model](#task-2-log-and-reload-a-model)
  - [Part 4: Model Registry](#part-4-model-registry)
    - [Task 1: Register a model](#task-1-register-a-model)
  - [Part 5: Serving Models (Bonus)](#part-5-serving-models-bonus)
    - [Task 1: Serve locally](#task-1-serve-locally)
  - [Lab Wrap-Up](#lab-wrap-up)
  - [Bonus Material](#bonus-material)

---

## Theory Overview

Today we focus entirely on **MLflow**, an open-source platform for managing the ML lifecycle.  
Key features include:

- **Experiment Tracking**: Logging hyperparameters, metrics, tags, and artifacts.
- **Model Management**: Logging and reloading models, comparing runs.
- **Model Registry**: Organizing models with lifecycle stages (`Staging`, `Production`).
- **Model Serving**: Exposing trained models as REST APIs.
- **UI Exploration**: Visualizing experiments and comparing results.

---

## Part 1: Getting Started with MLflow

### Task 1: Install and run MLflow UI

- Setup a local environment.

```bash
virtualenv .venv
source .venv/bin/activate
```

- Install MLflow in your local environment.

```bash
pip install mlflow scikit-learn matplotlib
mlflow ui
```

- Start the MLflow UI locally and explore the interface.
Open the MLflow UI at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Task 2: Autologging

- Train a simple scikit-learn model using `mlflow.autolog()`.

```python
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

mlflow.set_experiment("MLflow Autologging Demo")
mlflow.autolog()

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)

model = RandomForestRegressor(n_estimators=100, max_depth=5)
model.fit(X_train, y_train)
```

- Explore what MLflow logs automatically (params, metrics, artifacts).
Check UI for automatically logged results.

## Part 2: Manual Logging and Experiment Management

### Task 1: Log parameters, metrics, tags and the model manually

- Train several models with different hyperparameters.
- Log:
  - Hyperparameters
  - Accuracy (or other evaluation metric)
  - Tags to describe the run
  - The model itself

```python
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)

mlflow.set_experiment("MLflow Manual Logging")

with mlflow.start_run():
    params = {"solver": "lbfgs", "max_iter": 200}
    model = LogisticRegression(**params)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    mlflow.log_params(params)
    mlflow.log_metric("accuracy", acc)
    mlflow.set_tag("experiment", "baseline")
    mlflow.sklearn.log_model(model, name="model", input_example=X)
```

### Task 2: Compare runs in the UI

- Open MLflow UI.
- Compare multiple runs side by side by sorting on a chosen metric.
Select multiple runs → click Compare → sort by accuracy.

## Part 3: Working with Artifacts

### Task 1: Save artifacts (plots, preprocessing objects)

- Generate a visualization (e.g., confusion matrix or feature importance plot).
- Save the plot as an artifact in MLflow.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay.from_predictions(y_test, preds)
plt.savefig("confusion_matrix.png")

mlflow.log_artifact("confusion_matrix.png")
```

### Task 2: Log and reload a model

- Log a trained model as an MLflow artifact.
- Reload a trained model from MLflow and use it to make predictions.

```python
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Replace with the actual run_id printed in your training script
RUN_ID = "951d508729324079a172a1bcba3abc70"
MODEL_NAME = "model"

# Load the model back
model = mlflow.sklearn.load_model(f"runs:/{RUN_ID}/{MODEL_NAME}")

# Test on fresh data
X, y = load_iris(return_X_y=True)
_, X_test, _, y_test = train_test_split(X, y, random_state=42)

preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print("Predictions:", preds[:10])
print("Accuracy:", acc)
```

## Part 4: Model Registry

### Task 1: Register a model

- Choose one of your trained models and register it in MLflow Model Registry.
- Check out tags, description, promoting, versions.

```python
result = mlflow.register_model(model_uri=model_uri, name="iris_classifier")
```

## Part 5: Serving Models (Bonus)

### Task 1: Serve locally

- Serve a registered model locally with MLflow’s built-in REST API.

```bash
mlflow models serve -m runs:/951d508729324079a172a1bcba3abc70/model -p 1234 --no-conda
```

- Send requests via `curl` or Python `requests`.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"instances": [[5.1, 3.5, 3.4, 0.2]]}' \
http://127.0.0.1:1234/invocations
```

Or in Python:

```python
import requests

data = {"instances": [[5.1, 3.5, 1.4, 0.2]]}
res = requests.post("http://127.0.0.1:1234/invocations", json=data)
print(res.json())
```

## Lab Wrap-Up

- You learned how to:
  - Track experiments automatically and manually.
  - Log, compare, and reload models.
  - Register and manage models across lifecycle stages.
  - Serve models locally as REST APIs.
- This provides a foundation for later cloud integration (Azure ML, GCP).

---

## Bonus Material

- **Best Practices**:
  - Always log enough metadata (params, tags) for reproducibility.
  - Store artifacts like plots, configs, and preprocessing objects.
- **Useful Links**:
  - [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
  - [MLflow GitHub](https://github.com/mlflow/mlflow)
  - [MLflow Tracking Quickstart](https://mlflow.org/docs/latest/tracking.html)
