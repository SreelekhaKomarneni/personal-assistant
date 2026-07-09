from services.gmail_service import GmailService
from agent_tools import load_json

gmail_service = GmailService()

def get_emails(priority=None, sender=None, use_gmail=False):
    if use_gmail:
        return gmail_service.get_emails(priority=priority, sender=sender)
    
    emails = load_json("data/emails.json")

    if priority:
        emails = [
            email for email in emails
            if email.get("priority", "").lower() == priority.lower()
        ]

    if sender:
        emails = [
            email for email in emails
            if sender.lower() in email.get("from", "").lower()
        ]

    return emails