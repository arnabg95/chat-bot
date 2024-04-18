""" Email sending config """
from sendgrid import SendGridAPIClient
from app.config.settings import settings
from sendgrid.helpers.mail import Mail

# init sendgrid client with api key
sg = SendGridAPIClient(api_key=settings.SENDGRID_API)

def send_email(to:str, body: str, subject:str) -> None:
    """Send Email Using SendGrid.

    Args:
      to: Email of the receiver.
      body: Email body.
      subject: Email subject.
    """
    message = Mail(
        from_email=settings.FROM_EMAIL,
        to_emails=[to],
        html_content=body,
        subject=subject
    )
    try:
        sg.send(message)    
    except Exception as e:
        print(e)