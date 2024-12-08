import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def load_data():
    return pd.read_csv("solar_data.csv")

df = load_data()

st.title("Solar Data Dashboard")
selected_column = st.selectbox("Select a column to visualize", ['GHI', 'DNI', 'DHI', 'Tamb'])

st.subheader(f"Time-Series of {selected_column}")
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)
st.line_chart(df[selected_column])

if st.button("Show Correlation Heatmap"):
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)