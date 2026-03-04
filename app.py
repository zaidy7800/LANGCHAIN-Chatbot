from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load model
llm = ChatOllama(
    model="qwen2.5-coder:3b",
    temperature=0.7,
)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{question}"),
])

# Create chain (Correct order)
chain = prompt | llm | StrOutputParser()

# Invoke chain
response = chain.invoke({"question": "Hello, how are you?"})

# Print result
print(response)