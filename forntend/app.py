import streamlit as st
import requests
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📉",
    layout="wide"
)


st.markdown("""
<style>
body {
    background-color: #0b0f19;
}
.block-container {
    padding: 2rem 3rem;
}
h1, h2, h3 {
    color: #ffffff;
}
label {
    color: #cbd5e1 !important;
}
.glass {
    background: rgba(17, 24, 39, 0.95);
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    margin-bottom: 24px;
}
.low-risk {
    background: #064e3b;
    border-left: 6px solid #10b981;
    padding: 20px;
    border-radius: 12px;
    color: #ecfdf5;
}
.high-risk {
    background: #7f1d1d;
    border-left: 6px solid #ef4444;
    padding: 20px;
    border-radius: 12px;
    color: #fef2f2;
}
.stButton>button {
    width: 100%;
    padding: 12px;
    border-radius: 10px;
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


edu = {"Below College":1,"College":2,"Bachelor":3,"Master":4,"Doctor":5}
job_sat = {"Very Dissatisfied":1,"Dissatisfied":2,"Satisfied":3,"Very Satisfied":4}
env_sat = {"Poor":1,"Average":2,"Good":3,"Excellent":4}
job_inv = {"Low":1,"Medium":2,"High":3,"Very High":4}
wlb = {"Poor":1,"Fair":2,"Good":3,"Excellent":4}
perf = {"Low":1,"Good":2,"Excellent":3,"Outstanding":4}
job_lvl = {"Entry":1,"Junior":2,"Mid":3,"Senior":4,"Manager":5}


st.markdown("## 📉 Employee Attrition Prediction System")
st.caption("AI-powered HR analytics dashboard")


st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.subheader("👤 Employee Profile")

c1, c2, c3 = st.columns(3)

with c1:
    Age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=30,
    step=1
)
    DailyRate = st.number_input("Daily Rate", 100, 2000, 800)
    MonthlyIncome = st.number_input("Monthly Income", 1000, 50000, 5000)
    DistanceFromHome = st.slider("Distance From Home (km)", 0, 50, 5)
    Education = edu[st.selectbox("Education Level", edu.keys())]

with c2:
    JobLevel = job_lvl[st.selectbox("Job Level", job_lvl.keys())]
    TotalWorkingYears = st.slider("Total Working Years", 0, 40, 8)
    YearsAtCompany = st.slider("Years At Company", 0, 40, 5)
    NumCompaniesWorked = st.slider("Number of Companies Worked", 0, 10, 1)
    PercentSalaryHike = st.slider("Percent Salary Hike (%)", 5, 30, 13)

with c3:
    JobSatisfaction = job_sat[st.selectbox("Job Satisfaction", job_sat.keys())]
    EnvironmentSatisfaction = env_sat[st.selectbox("Environment Satisfaction", env_sat.keys())]
    JobInvolvement = job_inv[st.selectbox("Job Involvement", job_inv.keys())]
    WorkLifeBalance = wlb[st.selectbox("Work Life Balance", wlb.keys())]
    PerformanceRating = perf[st.selectbox("Performance Rating", perf.keys())]

predict = st.button("🚀 Predict Attrition")
st.markdown("</div>", unsafe_allow_html=True)

if predict:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("📊 Prediction Outcome")

    payload = {
        "Age": Age,
        "DailyRate": DailyRate,
        "MonthlyIncome": MonthlyIncome,
        "DistanceFromHome": DistanceFromHome,
        "Education": Education,
        "JobLevel": JobLevel,
        "TotalWorkingYears": TotalWorkingYears,
        "YearsAtCompany": YearsAtCompany,
        "NumCompaniesWorked": NumCompaniesWorked,
        "PercentSalaryHike": PercentSalaryHike,
        "JobSatisfaction": JobSatisfaction,
        "EnvironmentSatisfaction": EnvironmentSatisfaction,
        "JobInvolvement": JobInvolvement,
        "WorkLifeBalance": WorkLifeBalance,
        "PerformanceRating": PerformanceRating
    }

    with st.spinner("Analyzing attrition risk..."):
        result = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        ).json()["Attrition"]

    if result == "Yes":
        st.markdown("""
        <div class="high-risk">
            <h3>🔴 High Attrition Risk</h3>
            Immediate retention action recommended.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="low-risk">
            <h3>🟢 Low Attrition Risk</h3>
            Employee is likely to stay.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.subheader("📂 Bulk Prediction & Model Evaluation")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    if "Attrition" in df.columns:
        X = df.drop("Attrition", axis=1)
        y_true = df["Attrition"].map({"Yes":1,"No":0})

        preds = []
        for _, row in X.iterrows():
            res = requests.post(
                "http://127.0.0.1:8000/predict",
                json=row.to_dict()
            ).json()["Attrition"]
            preds.append(1 if res == "Yes" else 0)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Accuracy", f"{accuracy_score(y_true, preds):.2f}")
        c2.metric("Precision", f"{precision_score(y_true, preds):.2f}")
        c3.metric("Recall", f"{recall_score(y_true, preds):.2f}")
        c4.metric("F1 Score", f"{f1_score(y_true, preds):.2f}")
    else:
        st.error("CSV must contain 'Attrition' column")

st.markdown("</div>", unsafe_allow_html=True)

