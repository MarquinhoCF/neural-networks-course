from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # Dummy key
)
response = client.chat.completions.create(
    model="gemma-3-4b-it-qat",
    messages=[
        {"role": "user", "content": "Tell me a fun fact about space."}
    ]
)
print(response.choices[0].message.content)
