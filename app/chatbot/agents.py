""" create the openai agent here """

from langchain.agents import create_openai_tools_agent, AgentExecutor
from app.chatbot.llm import get_chat_llm
from app.chatbot.prompt import get_chat_prompt_template
from app.chatbot.tools import get_all_tools
from app.chatbot.memory import get_memory


def get_tools_agent():
    """create new openai tools agent"""
    return create_openai_tools_agent(
        llm=get_chat_llm(),
        tools=get_all_tools(),
        prompt=get_chat_prompt_template()
    )


def get_agent(guest_id: str, chat_id: str | None = None):
    """agent that will handle user query"""
    return AgentExecutor(
        agent=get_tools_agent(),
        tools=get_all_tools(),
        verbose=False,
        memory=get_memory(guest_id, chat_id),
    )
