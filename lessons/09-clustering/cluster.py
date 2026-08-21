# Step1-3：聚类全流程（标准化→KMeans→肘部→画像）
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

plt.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS"]
df = pd.read_csv("../../data/bank_customers.csv")
feats = ["balance", "avg_monthly_spend", "product_count", "overdue_count"]
X = StandardScaler().fit_transform(df[feats])

# Step2 肘部法则
sse = [KMeans(n_clusters=k, random_state=42, n_init=10).fit(X).inertia_
       for k in range(1, 10)]
plt.plot(range(1, 10), sse, marker="o"); plt.xlabel("k"); plt.ylabel("SSE")
plt.title("肘部法则（教学虚构数据）"); plt.savefig("outputs/elbow.png")

# Step1 + Step3：k=4 分群画像
df["cluster"] = KMeans(n_clusters=4, random_state=42, n_init=10).fit_predict(X)
print(df.groupby("cluster")[feats].mean().round(1))   # 检查点：均值画像表
print(df["cluster"].value_counts())
# 学生任务：给四簇起业务名（如"高余额低消费稳健型"）
