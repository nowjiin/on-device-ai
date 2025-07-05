from langchain_ollama import ChatOllama  # 이 부분 수정
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 수정: 모델명 변경
llm = ChatOllama(model="kwangsuklee/SEOKDONG-llama3.1_korean_Q5_K_M")