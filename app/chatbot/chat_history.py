""" create the class to store chat history using custom memory
to handle chat data in mongodb
"""

from typing import List
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import (
    BaseMessage, messages_from_dict, messages_to_dict)
from pymongo import MongoClient, errors
from app.utils.logger import logger


class MongoChatMessageHistory(BaseChatMessageHistory):
    """Chat message history that stores history in MongoDB.

    Args:
        connection_string: connection string to connect to MongoDB
        session_id: arbitrary key that is used to store the messages
            of a single chat session.
        database_name: name of the database to use
        collection_name: name of the collection to use
    """

    def __init__(
        self,
        guest_id: str,
        chat_id: str,
        db_url: str,
        db_name: str,
        schema_name: str,
    ):
        self.guest_id = guest_id
        self.chat_id = chat_id
        self.db_url = db_url
        self.db_name = db_name
        self.schema_name = schema_name

        try:
            self.client: MongoClient = MongoClient(self.db_url)
        except errors.ConnectionFailure as error:
            logger.error(error)

        self.db = self.client[self.db_name]
        self.collection = self.db[self.schema_name]

    @property
    def messages(self) -> List[BaseMessage]:  # type: ignore
        """Retrieve the messages from MongoDB"""
        try:
            cursor = list(self.collection.find({"chat_id": self.chat_id}))
        except errors.OperationFailure as error:
            logger.error(error)

        if len(cursor) > 0:
            messages = messages_from_dict(cursor)
        else:
            messages = []

        return messages

    def add_message(self, message: BaseMessage) -> None:
        """Append the message to the record in MongoDB"""
        try:
            messages = messages_to_dict(self.messages)
            msg = messages_to_dict([message])
            messages.append(msg[0])
            self.collection.insert_one(
                {
                    "chat_id": self.chat_id,
                    "guest_id": self.guest_id,
                    "type": msg[0]["type"],
                    "data": msg[0]['data'],
                }
            )

        except errors.WriteError as err:
            logger.error(err)

    def clear(self) -> None:
        """Clear the memory data from MongoDB"""
        try:
            self.collection.delete_many({"guest_id": self.guest_id})
        except errors.WriteError as err:
            logger.error(err)
