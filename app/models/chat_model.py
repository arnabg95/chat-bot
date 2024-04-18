"""chat model that will store all the messages"""

from pydantic import Field
from beanie import Document
from pymongo import IndexModel, ASCENDING
from datetime import datetime
from app.utils import chat_id_generator


class Chat(Document):
    """chat model to store chatbot messages"""

    guest_id: str
    chat_id: str = Field(
        default_factory=chat_id_generator.generate_chat_id_hex)
    type: str
    data: object

    createdAt: datetime = Field(default_factory=datetime.now)

    class Settings:
        """all the indexes"""

        indexes = [
            IndexModel([("createdAt", ASCENDING)], expireAfterSeconds=604800),
        ]
