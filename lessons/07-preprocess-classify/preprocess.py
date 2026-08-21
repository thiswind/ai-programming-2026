# Step1：建模前预处理（三板斧）
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("../../data/bank_customers.csv")
df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("未知")
df = pd.get_dummies(df, columns=["gender", "city", "risk_level"])
num_cols = ["balance", "avg_monthly_spend", "account_age_months"]
df[num_cols] = StandardScaler().fit_transform(df[num_cols])
print("处理后 shape:", df.shape)      # 检查点1：(200, ~20)
print(df.head(3))
