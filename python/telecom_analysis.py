import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
internet = pd.read_csv("internet_type.csv")
contract = pd.read_csv("contract.csv")
payment = pd.read_csv("payment_method.csv")
charge = pd.read_csv("charge_group.csv")

# ---------------- INTERNET ----------------
plt.figure()
sns.barplot(x="internet_type", y="churn_rate", data=internet)
plt.title("Churn Rate by Internet Type")
plt.savefig("internet_churn.png")

# ---------------- CONTRACT ----------------
plt.figure()
sns.barplot(x="contract", y="churn_rate", data=contract)
plt.title("Churn Rate by Contract Type")
plt.savefig("contract_churn.png")

# ---------------- PAYMENT ----------------
plt.figure()
sns.barplot(x="payment_method", y="churn_rate", data=payment)
plt.title("Churn Rate by Payment Method")
plt.xticks(rotation=30)
plt.savefig("payment_churn.png")

# ---------------- CHARGE ----------------
plt.figure()
sns.barplot(x="charge_group", y="churn_rate", data=charge)
plt.title("Churn Rate by Monthly Charges")
plt.savefig("charge_churn.png")

print("All charts saved successfully")
df = pd.read_csv("telecom_customer_churn.csv")

# 🔍 (Optional but useful)

print("Columns:", df.columns)

# ------------------------------

# R = Recency (tenure)

# ------------------------------

df['R_score'] = pd.qcut(df['Tenure in Months'], 3, labels=[3,2,1])

# ------------------------------

# F = Frequency (contract)

# ------------------------------

def freq_map(x):

    if x == "Month-to-month":

        return 1

    elif x == "One year":

        return 2

    else:

        return 3

df['F_score'] = df['Contract'].apply(freq_map)

# ------------------------------

# M = Monetary (monthly charge)

# ------------------------------

df['M_score'] = pd.qcut(df['Monthly Charge'], 3, labels=[1,2,3])

# ------------------------------

# Combine RFM

# ------------------------------

df['RFM_score'] = (

    df['R_score'].astype(str) +

    df['F_score'].astype(str) +

    df['M_score'].astype(str)

)

# ==============================

# 4. SEGMENTATION

# ==============================

def segment(row):

    if row['RFM_score'] == "333":

        return "Champion"

    elif int(row['R_score']) == 1:

        return "At Risk"

    else:

        return "Regular"

df['segment'] = df.apply(segment, axis=1)

# ==============================

# 5. OUTPUT

# ==============================

print(df[['RFM_score', 'segment']].head())


rfm_summary = df.groupby('segment').size().reset_index(name='customer_count')

rfm_summary.to_csv("rfm_output.csv", index=False)

print("RFM Analysis Completed ")

rfm_summary = df.groupby('segment').size().reset_index(name='customer_count')

print(rfm_summary)
