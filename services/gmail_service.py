class GmailService:
    def __init__(self):
        # Later this will store the authenticated Gmail API client
        self.gmail_client = None

    def get_emails(self, priority=None, sender=None):
        raise NotImplementedError(
            "Gmail API integration has not been implemented yet."
        )