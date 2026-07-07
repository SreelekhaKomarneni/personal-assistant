from tools.calendar_tools import get_calendar


def handle_calendar_request(date=None):
    return {
        "agent": "calendar_agent",
        "data": get_calendar(date=date)
    }