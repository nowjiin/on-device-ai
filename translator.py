from langchain_ollama import ChatOllama  # 이 부분 수정
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 수정: 모델명 변경
llm = ChatOllama(model="kwangsuklee/SEOKDONG-llama3.1_korean_Q5_K_M")

# 프롬프트 설정 최적화 (선택 사항)
prompt = ChatPromptTemplate.from_template(
    "다음 문장을 자연스러운 한국어로 번역해주세요:\n{input}"
)

# LangChain 표현식 언어 체인 구문을 사용합니다.
chain = prompt | llm | StrOutputParser()