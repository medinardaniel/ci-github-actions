"""Python Pandas Descriptive Statistics common functions"""
import pandas as pd
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
    col.value_counts().plot(kind='bar', color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return


def get_percentiles(df, column):
    """Percentiles function"""
    percentile_25 = np.percentile(df[column], 25)
    percentile_50 = np.percentile(df[column], 50)
    percentile_75 = np.percentile(df[column], 75)
    return percentile_25, percentile_50, percentile_75
