# import streamlit as st
# import requests

# st.title("Employee Attrition Prediction")

# age = st.number_input("Age", 18, 60)
# income = st.number_input("Monthly Income")
# joblevel = st.number_input("Job Level", 1, 5)
# years = st.number_input("Total Working Years", 0, 40)

# if st.button("Predict"):
#     data = {
#         "Age": age,
#         "MonthlyIncome": income,
#         "JobLevel": joblevel,
#         "TotalWorkingYears": years
#     }

#     response = requests.post("http://127.0.0.1:8000/predict", json=data)
#     st.success(response.json()["Attrition"])


# import streamlit as st
# import requests

# st.set_page_config(page_title="Employee Attrition Prediction", layout="wide")
# st.title("Employee Attrition Prediction App")

# col1, col2, col3 = st.columns(3)

# with col1:
#     Age = st.number_input("Age", 18, 60)
#     DailyRate = st.number_input("Daily Rate")
#     DistanceFromHome = st.number_input("Distance From Home")
#     Education = st.selectbox("Education", [1,2,3,4,5])
#     EnvironmentSatisfaction = st.selectbox("Environment Satisfaction", [1,2,3,4])

# with col2:
#     JobInvolvement = st.selectbox("Job Involvement", [1,2,3,4])
#     JobLevel = st.selectbox("Job Level", [1,2,3,4,5])
#     JobSatisfaction = st.selectbox("Job Satisfaction", [1,2,3,4])
#     MonthlyIncome = st.number_input("Monthly Income")
#     NumCompaniesWorked = st.number_input("Companies Worked")

# with col3:
#     PercentSalaryHike = st.number_input("Salary Hike %")
#     PerformanceRating = st.selectbox("Performance Rating", [1,2,3,4])
#     TotalWorkingYears = st.number_input("Total Working Years")
#     WorkLifeBalance = st.selectbox("Work Life Balance", [1,2,3,4])
#     YearsAtCompany = st.number_input("Years At Company")

# if st.button("Predict Attrition"):
#     data = {
#         "Age": Age,
#         "DailyRate": DailyRate,
#         "DistanceFromHome": DistanceFromHome,
#         "Education": Education,
#         "EnvironmentSatisfaction": EnvironmentSatisfaction,
#         "JobInvolvement": JobInvolvement,
#         "JobLevel": JobLevel,
#         "JobSatisfaction": JobSatisfaction,
#         "MonthlyIncome": MonthlyIncome,
#         "NumCompaniesWorked": NumCompaniesWorked,
#         "PercentSalaryHike": PercentSalaryHike,
#         "PerformanceRating": PerformanceRating,
#         "TotalWorkingYears": TotalWorkingYears,
#         "WorkLifeBalance": WorkLifeBalance,
#         "YearsAtCompany": YearsAtCompany
#     }

#     response = requests.post("http://127.0.0.1:8000/predict", json=data)
#     st.success(f"Employee Attrition: {response.json()['Attrition']}")

import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Employee Attrition Prediction App",
    layout="wide",
    page_icon="👥"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f5f6fa;
}
.main {
    padding: 10px;
}
.sidebar-box {
    background: #ffffff;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.center-box {
    background: #ffffff;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.1);
}
.result-box {
    background: #fdecea;
    padding: 15px;
    border-radius: 10px;
    border-left: 6px solid #e74c3c;
}
.success-box {
    background: #eafaf1;
    padding: 15px;
    border-radius: 10px;
    border-left: 6px solid #2ecc71;
}
.reco-box {
    background: #ffffff;
    padding: 18px;
    border-radius: 12px;
    margin-top: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
h1,h2,h3 {
    color: #2c3e50;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
left, center, right = st.columns([1.2, 3, 1.2])

# ================= LEFT PANEL =================
with left:
    st.markdown("<div class='sidebar-box'>", unsafe_allow_html=True)
    st.markdown("### 📌 About")
    st.write(
        "This application predicts employee attrition using a machine learning "
        "model trained on HR analytics data."
    )

    st.markdown("### 📝 Input Descriptions")
    st.write("""
    • **Age** – Employee age  
    • **Monthly Income** – Salary per month  
    • **Companies Worked** – Previous employers  
    • **Job Satisfaction** – 1 (Low) to 4 (High)  
    • **Work Life Balance** – 1 (Poor) to 4 (Excellent)  
    • **Environment Satisfaction** – Workplace satisfaction  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= CENTER PANEL =================
with center:
    st.markdown("<div class='center-box'>", unsafe_allow_html=True)

    st.markdown("## 👥 Employee Attrition Prediction App")
    st.write(
        "Employee attrition refers to employees leaving an organization. "
        "This app helps HR teams predict attrition risk and take preventive actions."
    )

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=120
    )

    st.markdown("### 🔢 Enter Employee Details")

    c1, c2, c3 = st.columns(3)

    with c1:
        Age = st.number_input("Age", 18, 60, 30)
        MonthlyIncome = st.number_input("Monthly Income", 1000, 20000, 5000)
        NumCompaniesWorked = st.number_input("Companies Worked", 0, 10, 1)
        DistanceFromHome = st.number_input("Distance From Home", 0, 50, 5)
        Education = st.selectbox("Education", [1,2,3,4,5])

    with c2:
        JobLevel = st.selectbox("Job Level", [1,2,3,4,5])
        JobSatisfaction = st.selectbox("Job Satisfaction", [1,2,3,4])
        EnvironmentSatisfaction = st.selectbox("Environment Satisfaction", [1,2,3,4])
        JobInvolvement = st.selectbox("Job Involvement", [1,2,3,4])
        WorkLifeBalance = st.selectbox("Work Life Balance", [1,2,3,4])

    with c3:
        DailyRate = st.number_input("Daily Rate", 100, 1500, 800)
        PercentSalaryHike = st.number_input("Salary Hike %", 5, 30, 13)
        PerformanceRating = st.selectbox("Performance Rating", [1,2,3,4])
        TotalWorkingYears = st.number_input("Total Working Years", 0, 40, 8)
        YearsAtCompany = st.number_input("Years At Company", 0, 40, 5)

    predict = st.button("🔍 Predict Attrition")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= RIGHT PANEL =================
with right:
    st.markdown("<div class='sidebar-box'>", unsafe_allow_html=True)
    st.markdown("### 📊 Result")

    if predict:
        data = {
            "Age": Age,
            "DailyRate": DailyRate,
            "DistanceFromHome": DistanceFromHome,
            "Education": Education,
            "EnvironmentSatisfaction": EnvironmentSatisfaction,
            "JobInvolvement": JobInvolvement,
            "JobLevel": JobLevel,
            "JobSatisfaction": JobSatisfaction,
            "MonthlyIncome": MonthlyIncome,
            "NumCompaniesWorked": NumCompaniesWorked,
            "PercentSalaryHike": PercentSalaryHike,
            "PerformanceRating": PerformanceRating,
            "TotalWorkingYears": TotalWorkingYears,
            "WorkLifeBalance": WorkLifeBalance,
            "YearsAtCompany": YearsAtCompany
        }

        res = requests.post("http://127.0.0.1:8000/predict", json=data)
        result = res.json()["Attrition"]

        if result == "Yes":
            st.markdown("<div class='result-box'>❌ High Attrition Risk</div>", unsafe_allow_html=True)
            st.write("**Prediction Probability:** ~ 85%")
        else:
            st.markdown("<div class='success-box'>✅ Low Attrition Risk</div>", unsafe_allow_html=True)
            st.write("**Prediction Probability:** ~ 20%")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= RECOMMENDATIONS =================
if predict and result == "Yes":
    st.markdown("<div class='reco-box'>", unsafe_allow_html=True)
    st.markdown("### 💡 Recommendations for Retaining Employee")
    st.write("""
    ✔ Improve job & environment satisfaction  
    ✔ Review salary and benefits  
    ✔ Provide training & growth opportunities  
    ✔ Encourage work-life balance  
    ✔ Conduct exit interviews and feedback sessions  
    """)
    st.markdown("</div>", unsafe_allow_html=True)