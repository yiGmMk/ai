import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
client = (
    OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)
)
model = os.getenv("MODEL","gemini-2.0-flash")


max_tokens = os.getenv("MAX_TOKENS", 100000)

print(f"Using model: {model}, MAX_TOKENS: {max_tokens}")

def call_openai(prompt: str, content: str) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
        max_tokens=8192,
        temperature=0.7,
        timeout=60,
    )
    return response.choices[0].message.content.strip()
