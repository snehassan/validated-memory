import hashlib
import json
import os
from pathlib import Path

from openai import OpenAI

# Talk to your vLLM server. Override with environment variables to use a hosted API later.
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "http://localhost:8471/v1"),
    api_key=os.getenv("LLM_API_KEY", "none"),
)

# Where cached responses are saved (already in .gitignore).
CACHE_DIR = Path("cache/llm")
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def call_llm(model, messages, temperature=0.0, max_tokens=1024):
    # 1. Build a unique key from everything that affects the output.
    request = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    key = hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()
    cache_file = CACHE_DIR / f"{key}.json"

    # 2. If we've made this exact call before, return the saved answer.
    if cache_file.exists():
        return json.loads(cache_file.read_text())

    # 3. Otherwise, ask the model.
    response = client.chat.completions.create(**request)

    # 4. Keep only what we need.
    result = {
        "text": response.choices[0].message.content,
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
    }

    # 5. Save it for next time, then return it.
    cache_file.write_text(json.dumps(result))
    return result