# 人工智能程序设计与实践 · 教师案例仓库（2026年秋季学期）

> 金融学+计算机科学与技术（双学士学位）2025级 ｜ 任课教师：胡矿
> 配套教材：《人工智能算法（Python 语言版）》胡矿，清华大学出版社

本仓库是课程的**复现对照基准**：每次课的课堂案例都在 `lessons/` 下，
每一步对应一个 git tag（如 `O1-step1`），课堂掉队可精确恢复：

```bash
git log --oneline --graph        # 看全课节奏
git diff O1-step2 O1-step3       # 看"这一步到底改了什么"
git checkout O1-step2            # 回到某一步继续
```

## 快速开始

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
cd lessons/01-compound-calculator
python compound_calc.py
```

## 目录

| 课次 | 目录 | 主题 | 教材章节 |
|---|---|---|---|
| 1 | lessons/01-compound-calculator | 首次人机协同循环：复利计算器 | 自编 |
| 2 | lessons/02-git-workflow | Git 工作流（停课，并入课次4讲授） | 自编 |
| 3 | lessons/03-pandas-report | pandas 数据初加工（停课，并入课次4讲授） | 自编 |
| 4 | lessons/04-ecosystem | 三课合并讲授：Git+pandas+生态地图（10/9） | 自编 |
| 5 | lessons/05-algorithm-basics | 复杂度与分治 | 第1、2章 |
| 6 | lessons/06-greedy-dp | 贪心与动态规划 | 第4、5章 |
| 7 | lessons/07-preprocess-classify | 预处理与决策树 | 第8章 |
| 8 | lessons/08-evaluation | 模型评估 | 第8章 |
| 9 | lessons/09-clustering | 聚类客户分群 | 第9章 |
| 10 | lessons/10-anomaly | LOF 异常检测 | 第10章 |
| 11 | lessons/11-patterns | Apriori 与综合实战 | 第11章 |
| 12 | lessons/12-neural-net | 神经网络 | 第14章 |
| 13 | lessons/13-llm-api | 大模型 API | 第17章 |
| 14 | lessons/14-rag-agent | RAG 与智能体 | 自编 |
| 15 | lessons/15-final | 期末答辩 | — |
| 16 | lessons/16-buffer | 机动 | — |


## 学生范例仓库

https://github.com/thiswind/ai-programming-2026-demo —— 示例同学的一学期完整作业形态（16课+HW1-3），
掉队或不确定作业长什么样时对照它。

## 数据集（data/，字段冻结）

见 `data/DATA_DICT.md`。**教学演示虚构数据，非真实统计**。
学生作业引用字段名必须与数据字典完全一致；改数值不改字段名。

## 学习资源

- llm2-isc.ynu.edu.cn：校内大模型平台（浏览器直用）
- TRAE CODE：trae.cn（免费 AI 原生 IDE）
- 教材附录 A 在线平台
