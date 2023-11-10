import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def generate_ts_data(seq_length):
    """Generates random time series data of specified sequence length."""
    return np.random.randn(seq_length)


def plot_ts_data(filepath):
    """Plots time series data from file into 3D scatter plot"""
    ts_data = np.genfromtxt(filepath)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(ts_data[:, 0], ts_data[:, 1], ts_data[:, 2])
    plt.savefig("ts_data_plot.png")


foo = generate_ts_data(25)
print(foo)

plot_ts_data(foo)

# print(plot_ts_data)
