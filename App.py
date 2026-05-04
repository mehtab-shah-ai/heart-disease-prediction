import streamlit as st
import pandas as pd
import joblib

# Load saved model, scaler, and expected columns
model            = joblib.load("knn_heart_model.pkl")
scaler           = joblib.load("heart_scaler.pkl")
expected_columns = joblib.load("heart_columns.pkl")

# ✅ Page config
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="🫀",
    layout="centered"
)

st.title("🫀 Heart Disease Prediction")
st.markdown("Fill in your medical details to check heart disease risk.")
st.markdown("---")

# ✅ 2 columns mein inputs
col1, col2 = st.columns(2)

with col1:
    age            = st.slider("Age", 18, 100, 40)
    sex            = st.selectbox("Sex", ["M", "F"])
    chest_pain     = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"],
                        help="ATA=Atypical, NAP=Non-Anginal, TA=Typical, ASY=Asymptomatic")
    resting_bp     = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol    = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
    fasting_bs     = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1],
                        format_func=lambda x: "Yes" if x == 1 else "No")  # ✅ 0,1 replace with Yes/No

with col2:
    resting_ecg    = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    max_hr         = st.slider("Max Heart Rate", 60, 220, 150)
    exercise_angina= st.selectbox("Exercise-Induced Angina", ["Y", "N"],
                        format_func=lambda x: "Yes" if x == "Y" else "No")  # ✅ Y/N replace with Yes/No
    oldpeak        = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
    st_slope       = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

st.markdown("---")

# Predict button
if st.button("🔍 Predict", use_container_width=True):

    raw_input = {
        'Age'                        : age,
        'RestingBP'                  : resting_bp,
        'Cholesterol'                : cholesterol,
        'FastingBS'                  : fasting_bs,
        'MaxHR'                      : max_hr,
        'Oldpeak'                    : oldpeak,
        'Sex_'          + sex        : 1,
        'ChestPainType_'+ chest_pain : 1,
        'RestingECG_'   + resting_ecg: 1,
        'ExerciseAngina_'+exercise_angina: 1,
        'ST_Slope_'     + st_slope   : 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df    = input_df[expected_columns]
    scaled_input= scaler.transform(input_df)
    prediction  = model.predict(scaled_input)[0]

    st.markdown("---")

    # ✅ Better result display
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease Detected!")
        st.markdown("""
        **Please consult a cardiologist immediately.**
        - Avoid strenuous activity
        - Monitor blood pressure regularly
        - Maintain a healthy diet
        """)
    else:
        st.success("✅ Low Risk of Heart Disease!")
        st.markdown("""
        **Keep maintaining a healthy lifestyle!**
        - Exercise regularly
        - Eat heart-healthy foods
        - Get regular checkups
        """)

# ✅ Footer
st.markdown("---")
st.caption("⚠️ This app is for educational purposes only. Not a substitute for medical advice.")
