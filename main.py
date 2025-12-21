import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('raw_churn_data.csv')

"""

#Total rows & columns - 7043 rows & 21 columns
print("Total rows & columns : ",df.shape)

#Target column → Churn
print("Target Column : " ,df['Churn'].value_counts())

#Numerical columns (tenure, charges, etc.)-'SeniorCitizen', 'tenure', 'MonthlyCharges'
print("Numerical columns : ",df.select_dtypes(include=['number']).columns)

#Categorical columns (contracst, payment method, etc.)
print("Categorical columns : ",df.select_dtypes(exclude=['number']).columns)


"""

#TotalCharges → it is wrongly read as text format
print(df["TotalCharges"].dtype)
df["TotalCharges"]=pd.to_numeric(df["TotalCharges"],errors="coerce").astype("float")

#Total null values in TotalCharges
print(df["TotalCharges"].isnull().sum())

#Rows with null TotalCharges
print(df[df["TotalCharges"].isna()])

#Replacing null TotalCharges with 0 where tenure is 0
df.loc[df["tenure"]==0,"TotalCharges"]=0

#Verifying null values are handled
print(df["TotalCharges"].isnull().sum())



print(df["tenure"])

#Create New Columns
conditions_tenure=[
    df["tenure"].between(0,12),
    df["tenure"].between(12,24),
    df["tenure"]>=24
]

choices_tenure=[
    "A",
    "B",
    "C"
]

df["tenure_group"]=np.select(conditions_tenure,choices_tenure,default="Not Specified")

print(df.columns)

print(df["MonthlyCharges"].describe())

conditions_MonthlyCharges=[
    df["MonthlyCharges"].between(0,30),
    df["MonthlyCharges"].between(30,64),
    df["MonthlyCharges"]>=64
]

choices_MonthlyCharges=[
    "Low",
    "Medium",
    "High"
]
df["charge_bucket"]=np.select(conditions_MonthlyCharges,choices_MonthlyCharges,default="Not Specified")

print(df["charge_bucket"].value_counts())