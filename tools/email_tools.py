def get_emails(priority=None, sender=None):
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