# Gender -> 1 Female 0 Male
# Churn -> 1 Yes 0 No
# Scaler is exported as scaler.pkl
# Model is exported as model.pkl
# Order of the x -> 'Age', 'Gender', 'Tenure', 'MonthlyCharges'
import streamlit as st
import joblib
import numpy as np
import os

st.write(os.listdir())

# LOAD model & scaler (NOT dump)
scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Customer Churn Prediction")

age = st.number_input("Age", 18, 100)
gender = st.selectbox("Gender", ["Female", "Male"])
tenure = st.number_input("Tenure", 0)
monthly_charges = st.number_input("Monthly Charges", 0)

if st.button("Predict"):
    gender_val = 1 if gender == "Male" else 0
    X = np.array([[age, gender_val, tenure, monthly_charges]])
    X_scaled = scaler.transform(X)

    pred = model.predict(X_scaled)[0]

    if pred == 1:
        st.error("YES , Customer WILL churn")
        st.balloons()
    else:
        st.success("NO, Customer will NOT churn")
        st.balloons()

    




    