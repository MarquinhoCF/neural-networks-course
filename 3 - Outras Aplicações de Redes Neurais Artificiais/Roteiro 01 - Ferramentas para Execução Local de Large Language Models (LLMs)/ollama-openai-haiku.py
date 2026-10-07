from openai import OpenAI

client = OpenAI(
    api_key='boguskey',
    base_url="http://localhost:11434/v1"
)

completion = client.chat.completions.create(
    model="llama3.2",
    temperature=1.0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)
print(completion.choices[0].message.content)
