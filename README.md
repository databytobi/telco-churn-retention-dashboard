# telco-churn-retention-dashboard
A data-driven churn retention dashboard built with Streamlit


📊 Telco Churn Retention Dashboard

Turning churn predictions into profitable retention decisions


---

1️⃣ Project Overview

Customer churn is a major revenue risk for telecom and SaaS companies. This project demonstrates a full end-to-end approach to:

Predict which customers are likely to churn

Quantify the revenue at risk

Recommend retention actions based on ROI


Goal: Focus on high-value, at-risk customers to maximize net savings while optimizing retention costs.


---

2️⃣ Dataset

Source: IBM Telco Customer Churn dataset

Key features:

Customer demographics: gender, Partner, Dependents

Service details: PhoneService, MultipleLines, InternetService, OnlineSecurity

Account info: Contract, PaymentMethod, PaperlessBilling, tenure, MonthlyCharges, TotalCharges

Target: Churn


Preprocessing & Feature Engineering:

value_segment (Low / Mid / High revenue)

tenure_group (New / Medium / Long)

churn_probability from XGBoost classifier

expected_loss & net_savings for retention ROI




---

3️⃣ Key Findings

Churn Insights

Insight	Observation

Contract Type	Month-to-month customers churn at >40%, two-year contracts <5%
Monthly Charges	Churned customers have higher median monthly charges (~$80 vs $65)
Tenure	Median tenure for churners is only 10 months vs 40 months for retained


Revenue at Risk

Top at-risk segment: Month-to-month, high-value customers

Revenue at risk: Concentrated among high-value customers

Retention simulation (budget-constrained):

Customers retained: 75

Total expected savings: $4,008

Total retention cost: $750

Net savings: $3,258



Interpretation: Targeting the right customers yields significant ROI while avoiding wasted retention spend.


---

4️⃣ Modeling Approach

Algorithms used:

Model	Precision (Churn=1)	Recall (Churn=1)	ROC-AUC

Logistic Regression	0.55	0.73	0.79
XGBoost	0.66	0.48	0.836


Notes:

Threshold adjustment: Optimized for net savings instead of raw accuracy

Feature importance: Contract, MonthlyCharges, Tenure, TechSupport are top predictors

Churn probability drives ROI-based retention decisions



---

5️⃣ Retention Strategy

ROI-based retention actions:

Action	Cost	Expected Save %

Discount	$15	40%
Support Call	$8	60%
Contract Upgrade	$5	20%


Only act on customers where Expected Saved Revenue − Retention Cost > 0

Focuses retention budget on high-value, high-risk customers



---

6️⃣ Dashboard

Built with Streamlit, the dashboard answers:

1. 💰 How much money is at risk?

Revenue exposure by value segment



2. 🎯 Who should we act on?

List of customers prioritized by net business value



3. 🛠 What action should we take?

Recommended retention action per customer



4. ⬇️ Export retention targets as CSV



Run locally:

streamlit run app.py


---

7️⃣ Skills & Tools Demonstrated

Python: pandas, NumPy, scikit-learn, XGBoost

Data preprocessing & feature engineering

Exploratory Data Analysis (EDA) & visual storytelling

Churn modeling, precision/recall optimization

ROI-based retention strategy

Streamlit dashboard development

Git & GitHub best practices (history clean-up, .gitignore)



---

8️⃣ Business Impact

Prioritized high-value churners to maximize ROI

Avoided wasted spend on low-risk customers

Demonstrated data-driven decision-making for retention campaigns

Ready for production deployment or presentation to stakeholders



---

9️⃣ Next Steps / Improvements

Include real-time billing and usage data

Add multi-class retention actions for more personalized campaigns

Deploy dashboard to  Heroku / AWS

Integrate email/SMS triggers for retention actions



Do you want me to do that next?
