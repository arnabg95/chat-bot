"""moderate user inputs"""

from openai import OpenAI
from app.config.settings import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def moderate_messages(message: str) -> bool:
    """
    run the message against openai to check
    if it can be passwd down to the llm
    """
    response = client.moderations.create(input=message)
    output = response.results[0].flagged
    return output