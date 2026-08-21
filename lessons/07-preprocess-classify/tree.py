# Step2+3：决策树训练与可视化
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree

df = pd.read_csv("../../data/bank_customers.csv")
df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("未知")
df = pd.get_dummies(df, columns=["gender", "city", "risk_level"])
num_cols = ["balance", "avg_monthly_spend", "account_age_months"]
df[num_cols] = StandardScaler().fit_transform(df[num_cols])

X = df.drop(columns=["customer_id", "is_default"])   # 切分前丢ID与标签！
y = df["is_default"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(Xtr, ytr)
print("测试集准确率:", accuracy_score(yte, clf.predict(Xte)))   # 检查点2
top = Xtr.columns[clf.feature_importances_.argmax()]
print("最顶层分裂特征:", top)

# 故意实验：不限深度 → 训练100% 测试更差（过拟合）
deep = DecisionTreeClassifier(max_depth=None, random_state=42).fit(Xtr, ytr)
print("不限深度 训练:", deep.score(Xtr, ytr), "测试:", deep.score(Xte, yte))

plt.figure(figsize=(14, 8))
plot_tree(clf, feature_names=X.columns, class_names=["正常", "违约"],
          filled=True, fontsize=8)
plt.savefig("outputs/tree.png")     # 检查点3：读出一条违约路径
print("树图已保存 outputs/tree.png")
