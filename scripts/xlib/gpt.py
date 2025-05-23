import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
client = (
    OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)
)
model = "gemini-2.0-flash"


def call_openai(prompt: str, content: str) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
        max_tokens=100000,
        temperature=0.7,
        timeout=600,
    )
    return response.choices[0].message.content.strip()
