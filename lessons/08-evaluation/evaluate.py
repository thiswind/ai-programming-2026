# Step1+2：混淆矩阵 / 分类报告 / ROC-AUC（含笨模型对照）
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (auc, classification_report, confusion_matrix,
                             roc_curve)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("../../data/bank_customers.csv")
df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("未知")
df = pd.get_dummies(df, columns=["gender", "city"])
# 教训：risk_level 由 is_default 生成，混入特征=标签泄漏（第7课陷阱，这里必须剔除）
df = df.drop(columns=["risk_level"])
num_cols = ["balance", "avg_monthly_spend", "account_age_months"]
df[num_cols] = StandardScaler().fit_transform(df[num_cols])
X = df.drop(columns=["customer_id", "is_default"]); y = df["is_default"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

# 笨模型：全预测不违约（故意实验）
print("违约率:", y.mean().round(2), "→ 笨模型准确率:", (1 - y.mean()).round(2))

clf = DecisionTreeClassifier(max_depth=4, random_state=42).fit(Xtr, ytr)
y_pred = clf.predict(Xte)
print("混淆矩阵:\n", confusion_matrix(yte, y_pred))
print(classification_report(yte, y_pred, target_names=["正常", "违约"], zero_division=0))

proba = clf.predict_proba(Xte)[:, 1]
fpr, tpr, _ = roc_curve(yte, proba)
print("决策树 AUC:", round(auc(fpr, tpr), 3))          # 检查点2

rf = RandomForestClassifier(n_estimators=100, random_state=42).fit(Xtr, ytr)
p2 = rf.predict_proba(Xte)[:, 1]
f2, t2, _ = roc_curve(yte, p2)
print("随机森林 AUC:", round(auc(f2, t2), 3))           # 自主实践对比

plt.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS"]
plt.plot(fpr, tpr, label="DecisionTree")
plt.plot(f2, t2, label="RandomForest")
plt.plot([0, 1], [0, 1], "k--", label="随机猜测 AUC=0.5")
plt.xlabel("FPR"); plt.ylabel("TPR"); plt.legend(); plt.title("ROC（教学虚构数据）")
plt.savefig("outputs/roc.png")
print("ROC 图已保存 outputs/roc.png")
