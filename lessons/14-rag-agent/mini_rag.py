# Step2：极简 RAG（三步：切片FAQ=现成小段→向量化检索→拼上下文生成）
import math
import os

from openai import OpenAI

client = OpenAI(base_url=os.environ["LLM_BASE_URL"],
                api_key=os.environ["LLM_API_KEY"])
EMB_MODEL = os.environ.get("EMB_MODEL", "text-embedding-v3")


def embed(texts):
    resp = client.embeddings.create(model=EMB_MODEL, input=texts)
    return [d.embedding for d in resp.data]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


faq = [line for line in open("../../data/faq_corpus.jsonl", encoding="utf-8")]
faq_vecs = embed(faq)                       # ① 切片（整条FAQ即小段）

question = "预留手机号怎么改"
qv = embed([question])[0]                   # ② 向量化检索
sims = sorted(((cosine(qv, v), i) for i, v in enumerate(faq_vecs)), reverse=True)
top2 = [i for _, i in sims[:2]]
print("命中 FAQ 编号:", [f"Q{i+1:03d}" for i in top2])

context = "\n".join(f"资料{i+1}: {faq[i]}" for i in top2)
resp = client.chat.completions.create(      # ③ 拼上下文生成（仅依据资料）
    model=os.environ.get("LLM_MODEL", "deepseek-chat"),
    messages=[{"role": "system",
               "content": "仅根据以下资料回答，未覆盖则说'知识库未覆盖'。"},
              {"role": "user", "content": f"{context}\n\n问题：{question}"}],
)
print(resp.choices[0].message.content)
