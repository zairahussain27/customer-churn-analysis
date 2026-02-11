# Customer Churn Analysis & Prediction | SQL, Python, Power BI

## 📌 Business Problem
Customer churn directly impacts revenue and growth.  
This project analyzes customer behavior to identify key factors driving churn and provides data-driven insights to improve customer retention.

---

## 📊 Dataset
- Industry: Telecom
- Records: Customer-level data
- Key features:
  - Tenure
  - Monthly Charges
  - Contract Type
  - Payment Method
  - Churn (Yes/No)

---

## 🛠 Tools Used
- SQL – Data analysis and business queries
- Power BI – Data visualization and dashboarding
- Excel / Python – Data cleaning
- GitHub – Version control and documentation

---

## 🔍 Analysis Approach
1. Data understanding and cleaning
2. Feature engineering (tenure groups, charge buckets)
3. SQL-based churn analysis
4. KPI creation
5. Interactive Power BI dashboard
6. Business insight generation

---

## 📈 Key Metrics
- Total Customers
- Churn Rate
- Average Tenure
- Average Monthly Charges
- Churn Rate by Segment

---

## 📌 Key Insights
- Month-to-month contract customers have the highest churn rate
- Customers with tenure less than 6 months are most likely to churn
- High monthly charges increase churn probability
- Electronic check users churn more than other payment methods
- Long-term contracts significantly reduce churn

---

## Project Outcome
- Identified high-risk customers likely to churn
- Provided business insights to improve retention
- Built interactive dashboard for decision making

---

## Project Structure
- data/ → dataset files
- notebook/ → analysis notebook
- dashboard/ → Power BI file
- README.md → project documentation
  
---
## 📊 Dashboard Preview
<img width="1272" height="714" alt="image" src="https://github.com/user-attachments/assets/2d42075d-1a13-405b-8798-9aed04144804" />
🔹 Insight 1 — Contract

Customers on month-to-month contracts have the highest churn rate compared to yearly and two-year contracts. Long-term contracts significantly improve retention.

🔹 Insight 2 — Tenure

Customers with tenure below one year show the highest churn, indicating early dissatisfaction or weak onboarding experience.

🔹 Insight 3 — Charges

Customers with higher monthly charges churn more frequently, suggesting pricing sensitivity and need for better value perception.

🔹 Insight 4 — Payment method

Customers using electronic check show higher churn than automatic payment users, indicating lower engagement or trust.

🔹 Insight 5 — Loyal segment

Customers with long tenure and yearly contracts show lowest churn, representing the most stable and profitable segment.

🔹 Insight 6 — Overall

Approximately ___% of customers have churned, representing a significant revenue risk and highlighting the need for targeted retention strategies.

---
## 💼 Business Recommendations
- Promote long-term contracts through discounts
- Offer onboarding support for new customers
- Provide loyalty rewards for high-tenure users
- Introduce pricing bundles for high-charge customers

---
## 📁 Repository Structure
📁 customer-churn-analysis
│
├── 📁 data
│   ├── raw_churn_data.csv              # Original raw dataset
│   └── cleaned_churn_data.csv          # Cleaned dataset used for analysis
│
├── 📁 notebooks
│   └── main.ipynb                      # Data cleaning, EDA and feature engineering
│
├── 📁 sql
│   └── churn_analysis.sql              # SQL queries for business analysis
│
├── 📁 dashboard
│   └── Churn Analysis.pbix             # Power BI dashboard file
│
├── 📁 docs
│   └── Information_Churn.txt           # Project notes & business insights
│
├── README.md                           # Project documentation
└── requirements.txt                    # Python libraries used
