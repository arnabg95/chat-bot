from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel ,EmailStr, Field
from app.chatbot.retrever import find_documents
from app.helpers import generate_html_for_email
from app.mail import mail_sender


class SendSummerySchema(BaseModel):
    name: str = Field(description="name of the user given in the chat",default=None)
    email: EmailStr = Field(description="email provided by the user during chat", default=None)
    summery: str = Field(description="summery of the conversation", default=None)

def send_summery_email(
        name: str = None, email: str = None, summery: str = None) -> None:
    try:
        if not name:
            raise ValueError("Name needed")
        if not email:
            raise ValueError("Email needed")
        if not summery:
            raise ValueError("Summery needed")
        
        htmlContent = generate_html_for_email.create_html_for_sales(name,email,summery)
        mail_sender.send_email(email, htmlContent, "New Project Estimation")
    except Exception as e:
        return f"the following error occured: {str(e)}"



run_send_email = StructuredTool.from_function(
    name="inform_sales_team",
    description="""Send email to sales team and the user.
    Use this tool when the user has confirmed the summery
    provided, Refrain from using made up name or email.""",
    func=send_summery_email,
    args_schema=SendSummerySchema
)



def use_retriver_get_data(query: str):
    """ 
    if in the user conversation, user
    is asking about the company weavers
    web solutions then you can use this
    function to retrive some data about
    the company. do not say made up things
    if you do not find the answer here.
    simply say you do not know. send the
    exact user query here
    """
    docs = find_documents(query)
    data = [d.page_content.lower() for d in docs]
    return " ".join(data) 


def get_all_tools():
    """return all the tools"""
    return [run_send_email]
