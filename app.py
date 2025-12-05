import streamlit as st
import numpy as np
import pickle

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤",
    layout="centered",
)

# ------------------ Load Model as clf ------------------
with open("clf.pkl", "rb") as file:
    clf = pickle.load(file)

# ------------------ Modern Title ------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#FF4B4B;'>
        ❤ Heart Disease Prediction App
    </h1>
    <p style='text-align:center; color:grey; font-size:18px;'>
        Enter the details below and get instant prediction with probability.
    </p>
    """,
    unsafe_allow_html=True,
)

# ------------------ Input Form ------------------
with st.container():
    st.subheader("Patient Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1, 120)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
        trestbps = st.number_input("Resting BP", 50, 200)

    with col2:
        chol = st.number_input("Cholesterol", 100, 600)
        fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
        restecg = st.selectbox("Rest ECG", [0, 1, 2])
        thalach = st.number_input("Max Heart Rate", 50, 250)

    col3, col4 = st.columns(2)

    with col3:
        exang = st.selectbox("Exercise Induced Angina", [0, 1])
        oldpeak = st.number_input("Oldpeak", 0.0, 10.0, step=0.1)

    with col4:
        slope = st.selectbox("Slope", [0, 1, 2])
        ca = st.selectbox("CA", [0, 1, 2, 3])
        thal = st.selectbox("Thal", [0, 1, 2])

# ------------------ Predict Button ------------------
st.markdown("---")

if st.button("🔍 Predict", use_container_width=True):
    sex_val = 1 if sex == "Male" else 0

    X = np.array([[age, sex_val, cp, trestbps, chol, fbs,
                   restecg, thalach, exang, oldpeak, slope,
                   ca, thal]])

    # Probability using clf
    proba = clf.predict_proba(X)
    heart_prob = proba[0][1] * 100  # Convert to %

    # ------------------ Result Box ------------------
    st.markdown("## 🔎 Prediction Result")

    if heart_prob > 50:
        st.markdown(
            f"""
            <div style="padding:20px; border-radius:10px;
                        background-color:#FFE5E5; color:#B30000;">
                <h3>⚠ High Risk of Heart Disease</h3>
                <p style="font-size:22px;">
                    Probability: <b>{heart_prob:.2f}%</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="padding:20px; border-radius:10px;
                        background-color:#E8FFE8; color:#006600;">
                <h3>✅ Low Risk of Heart Disease</h3>
                <p style="font-size:22px;">
                    Probability: <b>{heart_prob:.2f}%</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

