import numpy as np

import matplotlib.pyplot as plt


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    data.dropna(inplace=True)

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y


def plot_ecdf(series,
              xlabel,
              quantiles=None,
              ylabel='ECDF',
              title=None,
              figsize=(8, 8)):
    """Plot ecdf from series"""
    if quantiles:
        quantiles_y = quantiles
    else:
        quantiles_y = [0.1, 0.25, 0.5, 0.75, 0.9]

    x, y = ecdf(series)

    quantiles_x = np.quantile(x, quantiles_y)

    fig, ax = plt.subplots(figsize=figsize)
    plt.plot(x, y, marker='.', linestyle='none')
    plt.plot(quantiles_x, quantiles_y, marker='D',
             linestyle='none', color='blue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(('ECDF', 'Quantiles'), loc='lower right')

    if title:
        plt.title(title)

    for quantile_x, quantile_y in zip(quantiles_x, quantiles_y):
        print(f"Quantile {quantile_y*100}%: {quantile_x:.2f}")

    return
