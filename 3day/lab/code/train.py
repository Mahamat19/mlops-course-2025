import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_json("3day/lab/data/iris_clean.json")
X, y = df.drop("species", axis=1), df["species"]

model = LogisticRegression(max_iter=200)
model.fit(X, y)

with open("3day/lab/data/model.pkl", "wb") as f:
    pickle.dump(model, f)