# P3：缺失值处理（中位数填 age，"未知"填 city）
import pandas as pd

df = pd.read_csv("../../data/bank_customers.csv")
print("处理前缺失:\n", df.isna().sum())
df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("未知")
print("处理后缺失:\n", df.isna().sum())   # 检查点：应全为 0
