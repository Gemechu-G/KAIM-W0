import pandas as pd

def load_data(benin-malanville.csv):

    df = pd.read_csv(benin-malanville.csv)
    return df

if __name__ == "__main__":  
    df = load_data("solar_data.csv")
    print(df.head())  
 
    