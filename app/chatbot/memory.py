""" create the conversation buffer memory
that will store the current conversation in memory
"""

from langchain.memory.buffer import ConversationBufferMemory
from app.chatbot.chat_history import MongoChatMessageHistory
from app.config.settings import settings


def get_memory(guest_id: str, chat_id: str | None = None):
    """create and return buffer memory to retain the conversation info"""
    return ConversationBufferMemory(
        memory_key="messages",
        chat_memory=MongoChatMessageHistory(
            guest_id, chat_id, settings.DB_URL, settings.DB_NAME, "Chat"
        ),
        return_messages=True,
        input_key="content"
    )
