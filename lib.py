"""Python Pandas Descriptive Statistics common functions"""
import matplotlib.pyplot as plt
import numpy as np


def get_mean_median_mode(df, column):
    """Mean, Median, Mode function"""
    mean_val = np.mean(df[column])
    median_val = np.median(df[column])
    mode_val = df[column].mode()
    return mean_val, median_val, mode_val


def bar_chart(df, column, title, xlabel, ylabel, color):
    """Bar chart function"""
    col = df[column].str.upper()
    col.value_counts().plot(kind="bar", color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def get_percentiles(data_frame, column):
    """Percentiles function"""

    # Specify the desired percentiles as fractions (e.g., 0.25 for 25th percentile)
    percentiles = [0.25, 0.5, 0.75]  # Equivalent to 25th, 50th, and 75th percentiles

    # Calculate the percentiles for a specific column (e.g., column 'A')
    percentile_values = data_frame[column].quantile(q=percentiles)

    return percentile_values
