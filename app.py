import streamlit as st
import pickle
import numpy as np

# Load trained model
model7 = pickle.load(open("model7.pkl", "rb"))

st.title("❤️ Heart Disease Prediction App")
st.write("Fill the patient details below and check the risk of heart disease")

# Input fields
age = st.number_input("Age", 1, 120, 30)
sex = st.selectbox("Sex", ("Male", "Female"))
cp = st.selectbox("Chest Pain Type (1=typical angina, 2=atypical, 3=non-anginal, 4=asymptomatic)", (1, 2, 3, 4))
bp = st.number_input("Resting Blood Pressure (in mm Hg)", 50, 250, 120)
chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", (0, 1))
ekg = st.selectbox("Resting EKG results (0, 1, 2)", (0, 1, 2))
max_hr = st.number_input("Maximum Heart Rate Achieved", 50, 250, 150)
ex_angina = st.selectbox("Exercise Induced Angina (0=No, 1=Yes)", (0, 1))
st_depression = st.number_input("ST Depression Induced by Exercise", 0.0, 10.0, 1.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment (1, 2, 3)", (1, 2, 3))
num_vessels = st.selectbox("Number of Major Vessels Colored by Flouroscopy (0-3)", (0, 1, 2, 3))
thal = st.selectbox("Thallium (3=normal, 6=fixed defect, 7=reversible defect)", (3, 6, 7))

# Convert categorical value
sex = 1 if sex == "Male" else 0

# Prediction
if st.button("Predict"):
    features = np.array([[age, sex, cp, bp, chol, fbs, ekg, max_hr,
                          ex_angina, st_depression, slope, num_vessels, thal]])
    
    prediction = model7.predict(features)[0]
    
    if prediction == 1:
        st.error("⚠️ High risk of Heart Disease")
    else:
        st.success("✅ Low risk of Heart Disease")

