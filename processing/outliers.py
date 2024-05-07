import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def find_outliers(data):
    upper_bound = data.quantile(0.99)  # Calculate the 99th percentile
    indices = data > upper_bound  # Get a boolean series where True indicates an outlier
    return data[indices], indices

def histplot(data):
    sns.histplot(data, bins=40, kde=False, label='Data Distribution')
    plt.legend()
    plt.title('Histogram')
    plt.show()

