import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Prediction")

st.title("🎯 Student Performance Predictor")

model = pickle.load(open("models/model.pkl", "rb"))
encoder = pickle.load(open("models/encoder.pkl", "rb"))

gender = st.selectbox(
    "Gender",
    ["female", "male"]
)

race = st.selectbox(
    "Race/Ethnicity",
    ["group A","group B","group C","group D","group E"]
)

education = st.selectbox(
    "Parental Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)

lunch = st.selectbox(
    "Lunch",
    ["standard","free/reduced"]
)

prep = st.selectbox(
    "Test Preparation",
    ["none","completed"]
)

if st.button("Predict Performance"):

    data = pd.DataFrame({
        "gender":[gender],
        "race/ethnicity":[race],
        "parental level of education":[education],
        "lunch":[lunch],
        "test preparation course":[prep]
    })

    for col in data.columns:
        data[col] = data[col].astype("category").cat.codes

    prediction = model.predict(data)

    result = encoder.inverse_transform(prediction)[0]

    st.success(f"Predicted Performance: {result}")