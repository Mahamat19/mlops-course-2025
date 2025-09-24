import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Replace with the actual run_id printed in your training script
RUN_ID = "951d508729324079a172a1bcba3abc70"
MODEL_NAME = "model2"

# Load the model back
model = mlflow.sklearn.load_model(f"runs:/{RUN_ID}/{MODEL_NAME}")

# Test on fresh data
X, y = load_iris(return_X_y=True)
_, X_test, _, y_test = train_test_split(X, y, random_state=42)

preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print("Predictions:", preds[:10])
print("Accuracy:", acc)

# Register model
model_uri='m-79b86f52b1924ad2b1723e746b20bb7e'
result = mlflow.register_model(model_uri=model_uri, name="iris_classifier22")
