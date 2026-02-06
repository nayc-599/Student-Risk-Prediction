import streamlit as st

def get_user_input():
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
    
    return user_input

def preprocess_input(user_input):
    import pandas as pd

    support_map = {"None" : 0, 
                   "Low" : 1, 
                   "Moderate" : 2, 
                   "High" : 3, 
                   "Very High" : 4}
    
    education_map = {"None" : 0, 
                     "High School" : 1, 
                     "College" : 2, 
                     "Bachelor's" : 3, 
                     "Higher" : 4}
    
    yes_no = {"No" : 0,
               "Yes" : 1}

    user_df = pd.DataFrame({
        "Age": [user_input['age']],
        "StudyTimeWeekly": [user_input['study']],
        "Absences": [user_input['absences']],
        "ParentalSupport": [support_map[user_input['parental_support']]],
        "ParentalEducation": [education_map[user_input['parental_education']]],
        "Tutoring": [yes_no[user_input['tutoring']]],
        "Extracurricular": [yes_no[user_input['extracurricular']]],
        "Sports": [yes_no[user_input['sports']]],
        "Music": [yes_no[user_input['music']]],
        "Volunteering": [yes_no[user_input['volunteering']]]
    })

    return user_df 
