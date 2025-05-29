from sklearn.datasets import make_blobs
import pandas as pd
import os

def gerar_dados():
    X, y = make_blobs(n_samples=300, centers=3, n_features=2, random_state=42)
    df = pd.DataFrame(X, columns=["x1", "x2"])
    df["label"] = y

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/dados_sinteticos.csv", index=False)
    return X, y
