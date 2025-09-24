import pandas as pd

df = pd.read_json("3day/lab/data/iris2.json")
df = df.dropna()
df['petalWidth'] *= 2
df.to_json("3day/lab/data/iris_clean.json", index=False)