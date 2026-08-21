# Step2：流式输出（打字机效果）+ 首 token 延迟
import os
import time

from openai import OpenAI

client = OpenAI(base_url=os.environ["LLM_BASE_URL"],
                api_key=os.environ["LLM_API_KEY"])
stream = client.chat.completions.create(
    model=os.environ.get("LLM_MODEL", "deepseek-chat"),
    messages=[{"role": "user", "content": "用一段话介绍夏普比率"}],
    stream=True,
)
t0 = time.time(); first = True
for chunk in stream:
    delta = chunk.choices[0].delta.content or ""
    if delta:
        if first:
            print(f"[首 token 延迟 {time.time()-t0:.2f}s]"); first = False
        print(delta, end="", flush=True)
print()
