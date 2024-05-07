import pandas as pd
import scipy.stats as stats

def test_correlation(data, col1, col2):
    """
    Perform Pearson correlation test returning coeff, and p-value
    on non-NaN aligned pairs of col1 and col2.
    """
    sub_data = data[[col1, col2]].dropna()
    series1 = sub_data[col1]
    series2 = sub_data[col2]

    correlation_coeff, p_value = stats.pearsonr(series1, series2)
    return correlation_coeff, p_value