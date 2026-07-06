from tools.calendar_tools import get_calendar


def handle_calendar_request():
    events = get_calendar()
    return f"Calendar Agent found these events: {events}"