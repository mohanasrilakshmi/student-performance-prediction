import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard")

df = pd.read_csv(
    "data/StudentsPerformance.csv"
)

st.subheader("Dataset Overview")

st.dataframe(df.head())

fig = px.histogram(
    df,
    x="math score",
    title="Math Score Distribution"
)

st.plotly_chart(fig,
                use_container_width=True)

fig2 = px.scatter(
    df,
    x="reading score",
    y="writing score",
    color="gender"
)

st.plotly_chart(fig2,
                use_container_width=True)
