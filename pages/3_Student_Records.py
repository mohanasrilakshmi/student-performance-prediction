import streamlit as st
import pandas as pd

st.title("📋 Student Dataset")

df = pd.read_csv(
    "data/StudentsPerformance.csv"
)

st.dataframe(
    df,
    use_container_width=True
)