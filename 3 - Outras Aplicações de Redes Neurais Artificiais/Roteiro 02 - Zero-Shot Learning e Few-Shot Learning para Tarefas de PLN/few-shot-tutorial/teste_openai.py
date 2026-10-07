import os
from openai import OpenAI
# Conecta ao llama-server local
client = OpenAI(
    base_url="http://127.0.0.1:9999/v1",
    api_key="local"
)
# Few-shot examples for temperature conversion
few_shot_examples = [
    {"role": "user", "content": "Convert 0 Celsius to Fahrenheit."},
    {"role": "assistant", "content": "32 Fahrenheit"},
    {"role": "user", "content": "Convert 100 Celsius to Fahrenheit."},
    {"role": "assistant", "content": "212 Fahrenheit"}
]
# Main query for temperature conversion
main_query = {"role": "user", "content": "Convert 37 Celsius to Fahrenheit."}
# Combine system message, few-shot examples, and main query
messages = [
    {"role": "system", "content": "You are a helpful assistant that converts temperatures from Celsius to Fahrenheit."}
] + few_shot_examples + [main_query]
# Create a chat completion request
completion = client.chat.completions.create(
    model="DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf",
    messages=messages,
    temperature=0
)
# Print the response
print(completion.choices[0].message.content)