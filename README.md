# Student Risk Prediction Web App
Project Status: Complete

## Brief Description
A end-to-end classification pipeline that identifies student risk level to raise awareness and support proactive academic support.

## Purpose
This project aims to help educational instituions to proactively identify students who may be at risk of underperformance. By analysing historical academic data including attendance, grades and engagement metics, the application provides early warning signals that enable timely intervention. 

The interactive dashboard allows educators and students to:
- Explore key risk factors
- Simulate improvement strategies through what-if analysis
- Make data-driven decision in academic support programs

Ultimately, this tool serves to improve student outcomes by facilitatig personalised academic interventions before students fall too far behind.

## Features
- Predictive Modeling: Classification pipline using Logistic Regression (benchmarked against SVM and Random Forest Classifier)
- Model Optimisation: Hyper parameter tuning and class weight balancing
- Interactive Dashboard: Real-time scenario analysis built with Streamlit; students can adjust input to see risk level change
- Data Visualisation: Bar charts depicting probabilities of risk levels

## Tech Stack
- Python/Pandas: Data wrangling and feature engineering
- Scikit-learn: Machine learning models and evaluation
- Steamlit: Interactive web application
- Jupyter Notebook: Development and analysis

## Prequisites
- Python 3.8 or higher
- pip package manager

## Installation 
1. Clone the repository.

  ``


## Dataset
- 2,400 academic records
- Features: Age, Attendence, Parental Support, Parental Education, Tutoring, Extracurricular, Sports, Music, Volunteering
- Target: Risk level classification

## Model Performance
| Model | Weighted Precision | Weighted Recall | Weighted F-1 Score | Accuracy
| ------------- | ------------- | ------------- | ------------- | ------------- |
| SVM  | 0.80 | 0.79 | 0.79 | 0.79
| Random Forest Classifier  | 0.78 | 0.78 | 0.78 | 0.78
| Logistic Regression  | 0.84 | 0.83 | 0.83 | 0.83


## Future Improvements
- Implement deep learning models

## Licence
MIT
