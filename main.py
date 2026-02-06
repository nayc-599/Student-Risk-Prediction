from src.input_helper import preprocess_input
from src.predict_risk import predict_risk
from src.plot_charts import plot_charts

import streamlit as st
import joblib 

st.title("Student Risk Early Warning System")
st.write("""
Predicts a student's risk level based on study habits, parental support, and extracurricular involvement.
High-risk students can be flagged for timely intervention.
""")

model = joblib.load('models/student_risk_model.pkl')
scaler = joblib.load('models/scaler.pkl')

st.sidebar.header("Student Information")

user_input = {}
user_input['age'] = st.sidebar.number_input("Age", 0, 80, 16)
user_input['study'] = st.sidebar.slider("Study Time Weekly (Hours)", 0, 40, 5)
user_input['absences'] = st.sidebar.slider("Absences", 0, 30, 0)
user_input['parental_support'] = st.sidebar.selectbox("Parental Support", ["None", "Low", "Moderate", "High", "Very High"])
user_input['parental_education'] = st.sidebar.selectbox("Parental Education", ["None", "High School", "College", "Bachelor's", "Higher"])
user_input['tutoring'] = st.sidebar.radio("Tutoring", ["Yes", "No"], 1, horizontal=True)

col1, col2 = st.sidebar.columns(2)

with col1:
    user_input['extracurricular'] = st.radio("Extracurricular", ["Yes", "No"], 1, horizontal=True)
    user_input['sports'] = st.radio("Sports", ["Yes", "No"], 1, horizontal=True)
with col2:
    user_input['music'] = st.radio("Music", ["Yes", "No"], 1, horizontal=True)
    user_input['volunteering'] = st.radio("Volunteering", ["Yes", "No"], 1, horizontal=True)

user_df = preprocess_input(user_input)
user_data_scaled, predicted_risk_level, encoded_risk_level = predict_risk(user_df, model, scaler)

plot_charts(model, user_data_scaled, predicted_risk_level, encoded_risk_level)

