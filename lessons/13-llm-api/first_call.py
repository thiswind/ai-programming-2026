# Step1：首个 API 调用（key 走环境变量——红线：绝不硬编码）
import os

from openai import OpenAI

client = OpenAI(base_url=os.environ["LLM_BASE_URL"],
                api_key=os.environ["LLM_API_KEY"])
resp = client.chat.completions.create(
    model=os.environ.get("LLM_MODEL", "deepseek-chat"),
    messages=[{"role": "user", "content": "用三句话解释什么是复利"}],
)
print("模型:", resp.model)
print(resp.choices[0].message.content)   # 检查点1：三句话回答
