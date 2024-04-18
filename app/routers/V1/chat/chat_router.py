"""
auth routes file
all the auth related routes will
be defined here
"""

from fastapi import APIRouter
from app.models.chat_model import Chat
from app.schemas.message import Messages
from app.chatbot.chat import get_chat_instance


""" initialize the router """
router = APIRouter(prefix="/chat", tags=["Chatbot"])


@router.get("/get-chat-id-list/{guest_id}")
async def get_chat_ids_by_guest(guest_id: str):
    """get all the chat id"""
    data = await Chat.aggregate(
        [
            {"$match": {"guest_id": guest_id}},
            {"$project": {"_id": None, "chat_id": 1}},
            {"$group": {"_id": None, "chatIds": {"$addToSet": "$chat_id"}}},
        ]
    ).to_list()

    if len(data) > 0:
        return data[0]
    return []


@router.get("/get-chat-details/{chat_id}")
async def get_chat_details_by_id(chat_id: str):
    """get chat details by id"""
    data = await Chat.find(Chat.chat_id == chat_id).to_list()
    messages = []
    for item in data:
        messages.append({"text":item.data['content'], "type": "self" if item.data['type'] == "human" else "ai" })
    return messages


@router.post("/start-conversation")
async def start_convo(message: Messages):
    """
    we will initialize new chat instance with our prompt
    and return the messages to the frontend
    """

    chat = get_chat_instance(message.msg, message.guest_id, message.chat_id)
    return chat
