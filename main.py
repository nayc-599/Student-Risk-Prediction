from src.input_helper import preprocess_input, get_user_input
from src.predict_risk import predict_risk
from src.plot_charts import plot_charts

import streamlit as st
import joblib 

st.set_page_config(layout="wide")

st.title("Student Risk Early Warning System")
st.write("""
Predicts a student's risk level based on study habits, parental support, and extracurricular involvement.
High-risk students can be flagged for timely intervention.
""")

model = joblib.load('models/student_risk_model.pkl')
scaler = joblib.load('models/scaler.pkl')

st.sidebar.header("Student Information")

user_input = get_user_input()
user_df = preprocess_input(user_input)
user_data_scaled, predicted_risk_level, encoded_risk_level = predict_risk(user_df, model, scaler)

plot_charts(model, user_data_scaled, predicted_risk_level, encoded_risk_level)

