""" help generate html body for emails """


def convert_text_to_html(text):
    # Split the text into lines
    lines = text.split('\n')
       
    html = ""
    # Loop through each line of the text and convert it to HTML
    for line in lines:
        if line.strip() != '':
            # If the line is not empty, wrap it in a paragraph tag
            html += f'<p>{line}</p>\n'
    
    
    return html

def create_html_for_sales(name:str, email:str, summery:str):
    """Generate Html For Send Email TO Sales Team.
    
    Args:
        name: Name Of the client.
        email: Email of the client.
        summery: Summery of the conversation.
    
    Returns:
        Html In string format
    """
    return f"""Following Is The Information Of A Recent Conversation:\n\nName: {name}\nEmail: {email}\nSummery:\n{summery}
"""