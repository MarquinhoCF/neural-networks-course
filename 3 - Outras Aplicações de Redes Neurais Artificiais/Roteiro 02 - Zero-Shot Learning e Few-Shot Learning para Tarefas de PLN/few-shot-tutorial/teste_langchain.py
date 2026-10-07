from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI

# Define a prompt template for individual examples
example_pr = PromptTemplate(
    input_variables=["word", "definition"],
    template="Word: {word}\nDefinition: {definition}\n"
)

# Create a list of example dictionaries
examples = [
    {
        "word": "Artificial intelligence",
        "definition": "Machines programmed to emulate human thought processes and decision-making abilities."
    },
    {
        "word": "Euphoria",
        "definition": "A powerful feeling of both happiness and excitement."
    }
]

# Create the FewShotPromptTemplate with a prefix, examples, and suffix
prefix = "Provide a one-sentence definition for the following word."

suffix = "Word: {input}\nDefinition:"

few_shot_pr = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_pr,
    prefix=prefix + "\n\n",
    suffix=suffix,
    input_variables=["input"]
)

# Use the FewShotPromptTemplate to format a prompt for a new input
n_word = {"input": "Ephemeral"}

full_prompt = few_shot_pr.format(**n_word)

print(f"Prompt: {full_prompt}")

llm = ChatOpenAI(
    base_url="http://127.0.0.1:9999/v1",
    api_key="local"
)
response = llm.invoke(full_prompt)
print(f"Response: {response.content}")