""" create and return propmt template """

from langchain.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate
)
from .prompt_helpers import prompt_5


def get_chat_prompt_template():
    """generate and return the prompt
    template that will answer the users query
    """
    return ChatPromptTemplate(
        input_variables=["content", "messages", "context"],
        messages=[
            SystemMessagePromptTemplate.from_template(prompt_5),
            MessagesPlaceholder(variable_name="messages"),
            HumanMessagePromptTemplate.from_template("{content}"),
            MessagesPlaceholder("agent_scratchpad")
        ],
    )
