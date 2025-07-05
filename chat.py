from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 수정: 모델명 변경
llm = ChatOllama(model="kwangsuklee/SEOKDONG-llama3.1_korean_Q5_K_M")

# 프롬프트 설정 최적화 (선택 사항)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "당신은 도움이 되는 AI 비서입니다. 반드시 한국어로 자연스럽게 답변해야 합니다.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# LangChain 표현식 언어 체인 구문을 사용합니다.
chain = prompt | llm | StrOutputParser()