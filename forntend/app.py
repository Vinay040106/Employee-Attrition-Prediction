import streamlit as st
import requests
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Employee Attrition Prediction",
    layout="wide",
    page_icon="👤"
)

# ================= CSS =================
st.markdown("""
<style>
.block-container {
    padding: 1rem 2rem;
}
header, footer {visibility: hidden;}

body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.card {
    background: #111827;
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    margin-bottom: 20px;
}

h1, h2, h3 { color: white; }

label, .stSelectbox label, .stNumberInput label {
    color: #d1d5db !important;
}

.result-low {
    background: #064e3b;
    border-left: 6px solid #10b981;
    padding: 20px;
    border-radius: 12px;
    color: #ecfdf5;
}

.result-high {
    background: #7f1d1d;
    border-left: 6px solid #ef4444;
    padding: 20px;
    border-radius: 12px;
    color: #fef2f2;
}

.result-title {
    font-size: 22px;
    font-weight: 700;
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

# ================= VALUE MAPS =================
edu = {"Below College":1,"College":2,"Bachelor":3,"Master":4,"Doctor":5}
job_sat = {"Very Dissatisfied":1,"Dissatisfied":2,"Satisfied":3,"Very Satisfied":4}
env_sat = {"Poor":1,"Average":2,"Good":3,"Excellent":4}
job_inv = {"Low":1,"Medium":2,"High":3,"Very High":4}
wlb = {"Poor":1,"Fair":2,"Good":3,"Excellent":4}
perf = {"Low":1,"Good":2,"Excellent":3,"Outstanding":4}
job_lvl = {"Entry Level":1,"Junior":2,"Mid Level":3,"Senior":4,"Manager":5}

# ================= LAYOUT =================
left, center, right = st.columns([1.1, 3.2, 1.5])

# ================= LEFT =================
with left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 👤 About")
    st.write("""
    Machine learning system that predicts employee attrition risk
    using HR analytics data.

    **Features**
    - Single employee prediction
    - CSV bulk prediction
    - Model evaluation metrics
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ================= CENTER =================
with center:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## Employee Attrition Prediction")

    c1, c2, c3 = st.columns(3)

    with c1:
        Age = st.number_input("Age", 18, 60, 30)
        MonthlyIncome = st.number_input("Monthly Income", 1000, 20000, 5000)
        NumCompaniesWorked = st.number_input("Companies Worked", 0, 10, 1)
        DistanceFromHome = st.number_input("Distance From Home (km)", 0, 50, 5)
        Education = edu[st.selectbox("Education Level", edu.keys())]

    with c2:
        JobLevel = job_lvl[st.selectbox("Job Level", job_lvl.keys())]
        JobSatisfaction = job_sat[st.selectbox("Job Satisfaction", job_sat.keys())]
        EnvironmentSatisfaction = env_sat[st.selectbox("Environment Satisfaction", env_sat.keys())]
        JobInvolvement = job_inv[st.selectbox("Job Involvement", job_inv.keys())]
        PerformanceRating = perf[st.selectbox("Performance Rating", perf.keys())]

    with c3:
        DailyRate = st.number_input("Daily Rate", 100, 1500, 800)
        PercentSalaryHike = st.number_input("Salary Hike (%)", 5, 30, 13)
    
        TotalWorkingYears = st.number_input("Total Working Years", 0, 40, 8)
        YearsAtCompany = st.number_input("Years At Company", 0, 40, 5)
        WorkLifeBalance = wlb[st.selectbox("Work Life Balance", wlb.keys())]

    predict = st.button("🔍 Predict Attrition")
    st.markdown("</div>", unsafe_allow_html=True)

# ================= RIGHT =================
with right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📊 Prediction Result")

    if predict:
        payload = {
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

        result = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        ).json()["Attrition"]

        if result == "Yes":
            st.markdown("""
            <div class="result-high">
                <div class="result-title">❌ High Attrition Risk</div>
                Immediate retention action is recommended.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-low">
                <div class="result-title">✅ Low Attrition Risk</div>
                Employee is likely to stay.
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Enter details and click Predict")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= CSV UPLOAD & METRICS =================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 📂 Bulk Prediction & Model Evaluation")

uploaded_file = st.file_uploader("Upload CSV dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.markdown("### Dataset Preview")
    st.dataframe(df.head())

    if "Attrition" not in df.columns:
        st.error("CSV must contain 'Attrition' column")
    else:
        X = df.drop("Attrition", axis=1)
        y_true = df["Attrition"].map({"Yes":1,"No":0})

        preds = []
        for _, row in X.iterrows():
            res = requests.post(
                "http://127.0.0.1:8000/predict",
                json=row.to_dict()
            ).json()["Attrition"]
            preds.append(1 if res == "Yes" else 0)

        acc = accuracy_score(y_true, preds)
        prec = precision_score(y_true, preds)
        rec = recall_score(y_true, preds)
        f1 = f1_score(y_true, preds)

        st.markdown("### 📊 Model Metrics")
        a, b, c, d = st.columns(4)
        a.metric("Accuracy", f"{acc:.2f}")
        b.metric("Precision", f"{prec:.2f}")
        c.metric("Recall", f"{rec:.2f}")
        d.metric("F1 Score", f"{f1:.2f}")

st.markdown("</div>", unsafe_allow_html=True)

