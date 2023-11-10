import numpy as np
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt


def gen_time_series(n):
    # Generate random time series data with variable sequence length
    ts = []
    for i in range(n):
        seq_len = np.random.randint(50, 100)
        ts.append(np.random.normal(loc=0, scale=1, size=seq_len))
    df = pd.DataFrame({"Time": [i + 1 for i in range(n)]})
    df["Value"] = ts
    return df


def plot_ts(filename, imgname=""):
    if not filename:
        raise ValueError("Filename must be specified")
    if not imgname:
        raise ValueError("Image name must be specified")
    df = pd.read_csv(filename)
    fig, ax = plt.subplots()
    ax.plot(df["Time"], df["Value"])
    fig.savefig(imgname + ".png", dpi=300)


if __name__ == "__main__":
    n = int(input("Enter the number of data points to generate: "))
    df = gen_time_series(n)
    plot_ts(df, "image.png")
