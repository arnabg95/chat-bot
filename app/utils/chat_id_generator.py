""" generate chat id from uuid """

import uuid


def generate_chat_id_hex():
    """returns uuid in hex format"""
    return uuid.uuid4().hex
