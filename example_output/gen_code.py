import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def gen_time_series(n):
    # Generate random time series data with variable sequence length
    df = pd.DataFrame(
        {"Time": [i for i in range(n)], "Value": np.random.randint(0, 100, size=n)}
    )
    df.to_csv("data.csv", index=False)


def plot_ts(filename, imgname="graph.png"):
    # Read in time series data from CSV file
    df = pd.read_csv(filename)
    # Plot the data using Matplotlib
    fig, ax = plt.subplots()
    ax.plot(df["Time"], df["Value"])
    # Save the plot to an image file
    fig.savefig(imgname)


# Call the functions to generate and plot the time series data
gen_time_series(50)
plot_ts("data.csv", "graph.png")

