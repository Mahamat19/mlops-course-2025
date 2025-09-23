# Lab: Experiment Tracking with MLflow

## Table of Contents

- [Lab: Experiment Tracking with MLflow](#lab-experiment-tracking-with-mlflow)
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
- Install MLflow in your local environment.
- Start the MLflow UI locally and explore the interface.

### Task 2: Autologging

- Train a simple scikit-learn model using `mlflow.autolog()`.
- Explore what MLflow logs automatically (params, metrics, artifacts).

---

## Part 2: Manual Logging and Experiment Management

### Task 1: Log parameters, metrics, tags and the model manually

- Train several models with different hyperparameters.
- Log:
  - Hyperparameters
  - Accuracy (or other evaluation metric)
  - Tags to describe the run
  - The model itself

### Task 2: Compare runs in the UI

- Open MLflow UI.
- Compare multiple runs side by side by sorting on a chosen metric.

---

## Part 3: Working with Artifacts

### Task 1: Save artifacts (plots, preprocessing objects)

- Generate a visualization (e.g., confusion matrix or feature importance plot).
- Save the plot as an artifact in MLflow.

### Task 2: Log and reload a model

- Log a trained model as an MLflow artifact.
- Reload it from MLflow and use it to make predictions.

---

## Part 4: Model Registry

### Task 1: Register a model

- Choose one of your trained models and register it in MLflow Model Registry.
- Check out tags, description, promoting, versions.

---

## Part 5: Serving Models (Bonus)

### Task 1: Serve locally

- Serve a model locally with MLflow’s built-in REST API.
- Send requests via `curl` or Python `requests`.

---

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
