# P2：列选择与条件筛选（布尔索引）
import pandas as pd

df = pd.read_csv("../../data/bank_customers.csv")
km = df[df["city"] == "昆明"]
print("昆明客户数:", len(km))
rich_loan = df[(df["balance"] > 100000) & (df["loan_flag"] == 1)]
print("余额>10万且有贷款:", len(rich_loan))
print(df["risk_level"].value_counts())
# 故意实验：df["age"] > 40 单独运行返回什么？（布尔掩码）
