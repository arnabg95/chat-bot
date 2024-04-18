from pydantic import BaseModel
from typing import Optional


class Messages(BaseModel):
    guest_id: str
    chat_id: Optional[str] = None
    msg: str
