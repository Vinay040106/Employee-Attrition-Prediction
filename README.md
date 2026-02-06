# Employee-Attrition-Prediction
This project is an end-to-end Machine Learning web application designed to predict whether an employee is likely to leave an organization. It helps HR teams make data-driven retention decisions by identifying high-risk employees early.


## Project Overview

Employee attrition is a major challenge for organizations.  
This system helps HR teams **predict attrition risk in advance** and take proactive retention measures.

The application includes:
- A trained ML model for attrition prediction
- A REST API using FastAPI
- A professional HR dashboard using Streamlit

---

## Machine Learning Details

- **Dataset**: IBM HR Analytics Employee Attrition Dataset (Kaggle)
- **Model Used**: Random Forest Classifier
- **Target Variable**: Attrition (Yes / No)

### Features Used (15)
- Age  
- DailyRate  
- DistanceFromHome  
- Education  
- EnvironmentSatisfaction  
- JobInvolvement  
- JobLevel  
- JobSatisfaction  
- MonthlyIncome  
- NumCompaniesWorked  
- PercentSalaryHike  
- PerformanceRating  
- TotalWorkingYears  
- WorkLifeBalance  
- YearsAtCompany  

### Data Preprocessing
- Missing value handling
- Feature scaling using StandardScaler
- Label encoding
- Train-test split
  
---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Uvicorn
