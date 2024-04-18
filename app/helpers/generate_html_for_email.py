""" help generate html body for emails """

def create_html_for_sales(name:str, email:str, summery:str):
    """Generate Html For Send Email TO Sales Team.
    
    Args:
        name: Name Of the client.
        email: Email of the client.
        summery: Summery of the conversation.
    
    Returns:
        Html In string format
    """
    return f"""
    <div>
    <p>Following Is The Information Of A Recent Conversation:</p>
    <p>Name: {name}</p>
    <p>Email: {email}</p>
    <p>Summery: <br> {summery}</p>
    </div>
"""