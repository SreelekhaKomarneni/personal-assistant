from tools.email_tools import get_emails


def handle_email_request(priority=None, sender=None):
    return {
        "agent": "email_agent",
        "data": get_emails(priority=priority, sender=sender)
    }