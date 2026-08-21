# Step1+2：MLP vs KNN vs 决策树 + 损失曲线
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("../../data/bank_customers.csv")
df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("未知")
df = pd.get_dummies(df, columns=["gender", "city"])
df = df.drop(columns=["risk_level"])   # 标签泄漏特征剔除（同第8课）
num_cols = ["balance", "avg_monthly_spend", "account_age_months"]
df[num_cols] = StandardScaler().fit_transform(df[num_cols])
X = df.drop(columns=["customer_id", "is_default"]); y = df["is_default"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

mlp = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500,
                    random_state=42).fit(Xtr, ytr)
auc_mlp = roc_auc_score(yte, mlp.predict_proba(Xte)[:, 1])
auc_knn = roc_auc_score(yte, KNeighborsClassifier().fit(Xtr, ytr)
                        .predict_proba(Xte)[:, 1])
auc_tree = roc_auc_score(yte, DecisionTreeClassifier(max_depth=4, random_state=42)
                         .fit(Xtr, ytr).predict_proba(Xte)[:, 1])
print(f"MLP {auc_mlp:.3f} | KNN {auc_knn:.3f} | Tree {auc_tree:.3f}")

plt.plot(mlp.loss_curve_); plt.xlabel("iteration"); plt.ylabel("loss")
plt.title("MLP 损失曲线"); plt.savefig("outputs/loss.png")
# 故意实验：max_iter=10 → 损失还高准确率差（没训完）
