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