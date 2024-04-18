"""all codes related to chains"""

from langchain.chains.llm import LLMChain
from langchain.chains.moderation import OpenAIModerationChain
from app.chatbot.memory import get_memory
from langchain.chains.retrieval_qa.base import RetrievalQA
from app.chatbot.llm import get_chat_llm

def get_moderation_chain():
    """create and return moderation chain"""
    return OpenAIModerationChain()


def get_chain(llm, prompt, guest_id: str, chat_id: str | None = None):
    """generate and return llm chain instance"""
    return LLMChain(
        llm=llm,
        prompt=prompt,
        memory=get_memory(guest_id, chat_id),
        verbose=False
    )


def get_retriver(retriever):
    return RetrievalQA.from_chain_type(
    llm=get_chat_llm(),
    chain_type="stuff",
    retriever=retriever
)