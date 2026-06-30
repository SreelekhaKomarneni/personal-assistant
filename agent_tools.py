import json


def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


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

def get_calendar(date=None):
    events = load_json("data/calendar.json")

    if date:
        return [
            event for event in events
            if event.get("date") == date
        ]

    return events


def get_tasks(status=None):
    tasks = load_json("data/tasks.json")

    if status:
        return [
            task for task in tasks
            if task.get("status", "").lower() == status.lower()
        ]

    return tasks

def get_memory():
    return load_json("data/memory.json")