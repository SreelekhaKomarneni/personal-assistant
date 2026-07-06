from tools.email_tools import get_emails


def handle_email_request():
    return {
        "agent": "email_agent",
        "data": get_emails()
    }