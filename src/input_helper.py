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
