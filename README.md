# Student Risk Prediction Web App

![Status](https://img.shields.io/badge/Status-Complete-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An end-to-end machine learning application that identifies students at risk of academic underperformance, enabling proactive intervention and personalised support.

Try it out here:[studentriskprediction.streamlit.app]

## Purpose
This project empowers educational institutions to proactively identify students who may be at risk of underperformance. By analysing historical academic data—including attendance, grades, and engagement metrics, the application provides early warning signals that enable timely intervention. 

The interactive dashboard allows educators and students to:
- Explore key risk factors
- Simulate improvement strategies through what-if analysis
- Make data-driven decision in academic support programs

Ultimately, this tool serves to improve student outcomes by facilitatig personalised academic interventions before students fall too far behind.

## Features
- **Predictive Modeling**: Classification pipeline using Logistic Regression (benchmarked against SVM and Random Forest Classifier)
- **Model Optimisation**: Hyper parameter tuning and class weight balancing for high recall value
- **Interactive Dashboard**: Real-time scenario analysis built with Streamlit; students can adjust input to see risk level change
- **Data Visualisation**: Interactive depicting probability distribution across 4 risk levels

## Tech Stack
- **Python/Pandas**: Data wrangling and feature engineering
- **Scikit-learn**: Machine learning models and evaluation
- **Steamlit**: Interactive web application
- **Jupyter Notebook**: Development and analysis

## Prequisites
- Python 3.8 or higher
- pip package manager

## Installation 
1. Clone the repository.

    ``` bash
   git clone https://github.com/nayc-599/Student-Risk-Prediction.git
    ```
  
    ```bash
   cd Student-Risk-Prediction
    ```

3. Create and activate a virtual environment.

   ```bash
   python -m venv venv
   ```

   ```bash
   venv\Scripts\activate
   ```

   
5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
7. Run the streamlit app.
   
   ```bash
   streamlit run app.py
   ```

## Dataset

**Size:** 2,400 academic records

### Features 
- **Demographic:** Age
- **Academic Behavior:** Attendance rate
- **Family Support:** Parental support level, Parental education
- **Academic Support:** Tutoring participation
- **Engagement:** Extracurricular activities, Sports, Music, Volunteering

### Target Variable
- **Multi-class classification:** Low Risk, Medium Risk, High Risk, Very High Risk
- **Class distribution:** ~70.5% high to very high risk students (imbalanced dataset)

## Model Performance
### Benchmark results
| Model | Weighted Precision | Weighted Recall | Weighted F-1 Score | Accuracy
| ------------- | ------------- | ------------- | ------------- | ------------- |
| **Logistic Regression**  | **0.84** | **0.83** | **0.83** | **0.83**
| SVM  | 0.80 | 0.79 | 0.79 | 0.79
| Random Forest Classifier  | 0.78 | 0.78 | 0.78 | 0.78

### Selected Model Classification Report
**Logistic Regression**
| Class | Precision | Recall | F1-score | Support |
|------:|----------:|-------:|---------:|--------:|
| 0     | 0.81      | 0.85   | 0.83     | 65      |
| 1     | 0.71      | 0.70   | 0.70     | 80      |
| 2     | 0.62      | 0.75   | 0.68     | 85      |
| 3     | 0.97      | 0.89   | 0.92     | 249     |
| **Accuracy** | — | — | **0.83** | **479** |
| **Macro Avg** | 0.78 | 0.80 | 0.78 | 479 |
| **Weighted Avg** | 0.84 | 0.83 | 0.83 | 479 |
- Achieves 83% overall accuracy in classifying student risk levels.
- Demonstrates strong recall for higher-risk groups, identifying 75% of high-risk students (Class 2) and 89% of very high-risk students (Class 3).
- Very high precision for Class 3 (0.97), indicating minimal false positives when predicting very high risk.

### Why this matters
- High precision for Class 3 reduces unneccesary intervations and allows educators to allocate resources more sustainably
- High recall for Classes 2 and 3 allows prioritisation of catching vulnerable students rather than missing them, allowing for timely academic support.

## Dashboard Screenshot
<img width="1909" height="944" alt="image" src="https://github.com/user-attachments/assets/a704faa8-26cd-47e8-97e1-00aec659667f" />

## Project Structure
Student-Risk-Prediction
├── data
├── models                   
│   ├── student_risk_model.pkl 
│   └── 
└── ...

## Future Improvements
- Adjust decision threshold to priroritise higher recall (fewer false positives)
- Allow dataset customisation/uploading
- Add new page on overall student risk distribution
- Experiment with deep learning models
- Track individual student risk over time

## Contributing
Contributions, issues and features requests are welcome!

### How to contribute
1. Fork the repository.
2. Create feature branch.
   ```bash
   git checkout -b feature/SomeFeature
   ```
3. Commit changes.
    ```bash
    git commit -m 'Add some feature'
    ```
    
4. Push to branch.
    ```bash
    git push feature/SomeFeature
    ```
   
5. Open a Pull Request.
  
## Licence
MIT

## Author/Contact


## Acknowledgement
- Data Source [https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset]
- Sci-kit learn community for excellent documentation
- Streamlit for the amazing framework
