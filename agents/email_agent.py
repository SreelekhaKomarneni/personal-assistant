from tools.email_tools import get_emails


def handle_email_request():
    emails = get_emails()
    return f"Email Agent found these emails: {emails}"