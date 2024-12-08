import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_summary(df):
    """Prints summary statistics."""
    print(df.describe())

def plot_time_series(df):
    """Plots time-series data."""
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    df[['GHI', 'DNI', 'DHI']].plot(figsize=(10, 5))
    plt.title("Solar Irradiance Over Time")
    plt.show()

def plot_correlation_heatmap(df):
    """Plots a correlation heatmap."""
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("solar_data.csv")
    generate_summary(df)
    plot_time_series(df)
    plot_correlation_heatmap(df)