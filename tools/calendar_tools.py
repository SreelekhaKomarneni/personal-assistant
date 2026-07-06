from agent_tools import load_json


def get_calendar(date=None):
    events = load_json("data/calendar.json")

    if date:
        return [
            event for event in events
            if event.get("date") == date
        ]

    return events