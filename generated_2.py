import numpy as np
import matplotlib.pyplot as plt
from mplfinance import savefig

# what is mplfinance?


def generate_ts_data(seq_length):
    """Generates random time series data of specified sequence length."""
    return np.random.randn(seq_length)


def plot_ts_data(file_path):
    """Plots time series data from file and saves it as an image"""
    ts_data = np.loadtxt(file_path, delimiter=",")
    fig = plt.figure()
    ax = fig.add_subplot(111, ylabel="Time Series Data")
    ax.plot(ts_data)
    savefig(f"{file_path}.png")


# Example usage
sequence_length = 50
ts_data = generate_ts_data(sequence_length)
plot_ts_data("ts_data.csv")
