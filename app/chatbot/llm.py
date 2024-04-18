""" langchaion chatbot code """

from langchain_openai import ChatOpenAI
from app.config.settings import settings


def get_chat_llm():
    """create and return a new chat llm object"""
    return ChatOpenAI(
        api_key=settings.OPENAI_API_KEY,
        model="gpt-3.5-turbo",
        verbose=False,
        temperature=0
    )
