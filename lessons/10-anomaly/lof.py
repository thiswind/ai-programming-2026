# Step1+2：LOF 检测可疑交易（不使用 is_fraud！）
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

df = pd.read_csv("../../data/transactions.csv")
df["day_count"] = df.groupby(["customer_id", "txn_date"])["txn_id"].transform("count")
feats = df[["amount", "txn_hour", "day_count"]]

lof = LocalOutlierFactor(n_neighbors=20)
labels = lof.fit_predict(feats)
df["score"] = -lof.negative_outlier_factor_       # 越大越异常
sus = df.sort_values("score", ascending=False).head(15)
print(sus[["txn_id", "customer_id", "amount", "txn_hour", "score"]])
# 检查点1：名单中"凌晨大额"特征占多数

thr = df["score"].quantile(0.985)                  # Step2 前1.5%阈值
print(f"阈值 {thr:.2f}，可疑 {int((df['score'] > thr).sum())} 笔")
print("给风控经理：建议对上述凌晨大额交易人工核查（教学虚构数据）")
