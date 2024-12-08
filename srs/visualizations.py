import pandas as pd
import matplotlib.pyplot as plt

def plot_histograms(df, column, bins=20):
    """Plots a histogram for the given column."""
    df[column].hist(bins=bins)
    plt.title(f"{column} Distribution")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("solar_data.csv")
    plot_histograms(df, "GHI")