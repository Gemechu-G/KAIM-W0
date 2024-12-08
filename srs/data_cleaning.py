import pandas as pd
from scipy.stats import zscore

def clean_data(df):
  df.fillna(df.mean(), inplace=True)  
    df['zscore'] = zscore(df['GHI'])
    df = df[df['zscore'].abs() <= 3]  
    df.drop(columns=['zscore'], inplace=True)
    return df

if __name__ == "__main__":
    df = pd.read_csv("solar_data.csv")
    df_clean = clean_data(df)
    print(df_clean.info())