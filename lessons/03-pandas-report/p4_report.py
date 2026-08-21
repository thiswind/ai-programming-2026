# P4：分组统计与可视化（中文乱码处理）
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS"]  # 中文
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("../../data/bank_customers.csv")
city_bal = df.groupby("city")["balance"].mean()
print(city_bal)
ax = city_bal.plot(kind="bar", title="六城平均存款余额（教学虚构数据）")
ax.set_xlabel("城市"); ax.set_ylabel("平均余额（元）")
plt.tight_layout()
plt.savefig("outputs/city_balance.png")   # 检查点：图入库
print("图已保存 outputs/city_balance.png")

df["age"].plot(kind="hist", bins=20, title="客户年龄分布（教学虚构数据）")
plt.savefig("outputs/age_hist.png")
