""" handle chat related codes """

from app.chatbot.agents import get_agent
from langchain.globals import set_debug
import uuid
from app.chatbot.moderate import moderate_messages
from app.chatbot.tools import use_retriver_get_data

set_debug(False)

def get_chat_instance(user_message: str, guest_id: str,
                      chat_id: str | None = None):
    """create and return an instace of the agent"""
    if not chat_id:
        chat_id = uuid.uuid4().hex

    agent = get_agent(guest_id, chat_id)
    related_doc = use_retriver_get_data(user_message)
    res = agent.invoke({"content": user_message, "context": related_doc})
    return {"message": res["output"], "chat_id": chat_id}
    # if moderate_messages(user_message):
    #     return { "message": "Your input goes against our policies." }
    # else:
    #     related_doc = use_retriver_get_data(user_message)
    #     res = agent.invoke({"content": user_message, "context": related_doc})
    #     return {"message": res["output"], "chat_id": chat_id}
