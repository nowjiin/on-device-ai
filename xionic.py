from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser


llm = ChatOllama(model="kwangsuklee/SEOKDONG-llama3.1_korean_Q5_K_M")

# Prompt 설정
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful, smart, kind, and efficient AI assistant"
            "You always fulfill the user's requests to the best of your ability."
            "You must generate an answer in Korean.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | llm | StrOutputParser()
