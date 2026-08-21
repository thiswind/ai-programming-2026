# P1：读入与初识（三连：head/info/describe）
import pandas as pd

df = pd.read_csv("../../data/bank_customers.csv")
print(df.head())          # 看前5行长啥样
print(df.info())          # 看列类型和缺失
print(df.describe())      # 看数值分布概要
print("shape:", df.shape)  # 检查点：200 行 12 列
