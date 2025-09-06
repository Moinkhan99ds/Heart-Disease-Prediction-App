import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("❤️ Heart Disease Prediction App")

st.write("Fill in the details below to predict if the patient has heart disease.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ("Male", "Female"))
cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, value=0)
bp = st.number_input("Resting Blood Pressure", min_value=50, max_value=250, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", (0, 1))
ekg = st.number_input("Resting ECG Results (0-2)", min_value=0, max_value=2, value=1)
max_hr = st.number_input("Maximum Heart Rate", min_value=50, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina", (0, 1))
st_depression = st.number_input("ST Depression", min_value=0.0, max_value=10.0, value=1.0, format="%.1f")
slope = st.number_input("Slope of ST Segment (0-2)", min_value=0, max_value=2, value=1)
ca = st.number_input("Number of Vessels Colored by Fluoroscopy (0-3)", min_value=0, max_value=3, value=0)
thal = st.number_input("Thallium (0-3)", min_value=0, max_value=3, value=1)

# Prediction button
if st.button("Predict"):
    # Encode sex as numeric
    sex_val = 1 if sex == "Male" else 0

    # Arrange features as per training dataset
    features = np.array([[age, sex_val, cp, bp, chol, fbs, ekg,
                          max_hr, exang, st_depression, slope, ca, thal]])
 prediction = model.predict(features)

    # Display result
    if prediction[0] == 1:
        st.error("🚨 The person is likely to have Heart Disease.")
    else:
        st.success("✅ The person is unlikely to have Heart Disease.")
