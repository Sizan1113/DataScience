import streamlit as st
import requests

API_URL = 'https://logistic-api-3.onrender.com/predict-termination'

st.title("Emoloyee termination Prediction")

st.sidebar.header("Employee details")
empSatisfaction = st.sidebar.slider(
    "Employee-Satisfaction",
    max_value=5,
    min_value=0,
    value=3,
    step=1
)
specialProjectsCount = st.sidebar.slider(
    "Special-Projects",
    max_value=20,
    min_value=0,
    value=3,
    step=1
)
absences = st.sidebar.slider(
    "Absenses",
    max_value=20,
    min_value=0,
    value=3,
    step=1
)

if st.sidebar.button("Predict Termination or Active"):
    payload = {
        "EmpSatisfaction": empSatisfaction,
        "SpecialProjectsCount": specialProjectsCount,
        "Absences": absences
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            if result["predicted Termination"] == 1:
                st.error("Employee is likely to be terminated.")
            else:
                st.success("Employee is likely to be active.")
        else:
            st.error("API ERROR!!")
    except requests.exceptions.RequestException:
        st.error("Could not connect to API. Please try again later.")
