# Step1：关联规则挖掘（支持度0.05 置信度0.5）
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv("../../data/transactions.csv")
# 篮子单位 = 客户×日（同日共现才有营销意义；按客户会把半年全混在一起）
df["month"] = df["txn_date"].str[:7]
basket = (df.groupby(["customer_id", "txn_date"])["merchant_type"]
            .value_counts().unstack(fill_value=0).astype(bool))
freq = apriori(basket, min_support=0.02, use_colnames=True)
rules = association_rules(freq, metric="confidence", min_threshold=0.1)
print(rules.sort_values("lift", ascending=False)
      [["antecedents", "consequents", "support", "confidence", "lift"]]
      .head(10))
# 检查点：应出现"购物→娱乐"类强规则（数据已预埋共现）
