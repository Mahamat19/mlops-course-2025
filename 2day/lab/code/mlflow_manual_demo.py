import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)

mlflow.set_experiment("MLflow Manual Logging")

with mlflow.start_run():
    params = {"solver": "lbfgs", "max_iter": 200}
    model = LogisticRegression(**params)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # Log params, metrics, set tags, save model.
    mlflow.log_params(params)
    mlflow.log_metric("accuracy", acc)
    mlflow.set_tag("experiment", "baseline")
    mlflow.sklearn.log_model(model, name="model", input_example=X)

    # Save confusion matrix locally.
    disp = ConfusionMatrixDisplay.from_predictions(y_test, preds)
    plt.savefig("confusion_matrix.png")

    # Save confusion matrix as an artifact.
    mlflow.log_artifact("confusion_matrix.png")