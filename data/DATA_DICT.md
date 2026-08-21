# 数据字典 DATA_DICT（字段名冻结）

> 教学演示虚构数据，非真实统计。字段名一经发布不可更改（讲义/仓库/评价系统三方引用）；教师只可改数值。

## bank_customers.csv（200 行）
| 字段 | 类型 | 含义 |
|---|---|---|
| customer_id | str | 客户编号 C0001-C0200 |
| age | int | 年龄 18-70（预埋缺失 8 行） |
| gender | str | 性别 男/女 |
| city | str | 城市（云南 6 城；预埋缺失 5 行） |
| account_age_months | int | 开户月数 1-240 |
| product_count | int | 持有产品数 1-8 |
| balance | float | 存款余额（元） |
| avg_monthly_spend | float | 月均消费（元）（预埋 5 行极端离群） |
| loan_flag | int | 是否有贷款 0/1 |
| overdue_count | int | 历史逾期次数 0-6 |
| is_default | int | 是否违约 0/1（标签列，违约率约 15%） |
| risk_level | str | 风险评级 低/中/高 |

## transactions.csv（1000+ 行）
| 字段 | 类型 | 含义 |
|---|---|---|
| txn_id | str | 交易编号 |
| customer_id | str | 客户编号（外键） |
| txn_date | str | 交易日期 2026-01-01 至 2026-06-30 |
| txn_hour | int | 交易小时 0-23 |
| amount | float | 交易金额（元） |
| channel | str | 渠道 柜台/APP/网银/ATM |
| merchant_type | str | 商户类别 超市/餐饮/转账/缴费/娱乐/购物 |
| is_fraud | int | 是否欺诈（评估暗桩，学生任务中禁止引用） |

## faq_corpus.jsonl（60 条）
| 字段 | 含义 |
|---|---|
| q_id | 问题编号 |
| question | 客户问题 |
| answer | 标准答案 |
| category | 分类 账户/银行卡/贷款/理财/安全 |
