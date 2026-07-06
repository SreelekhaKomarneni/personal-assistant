from agents.email_agent import handle_email_request
from agents.calendar_agent import handle_calendar_request
from agents.task_agent import handle_task_request
from agents.memory_agent import handle_memory_request


def route_request(user_question):
    question = user_question.lower()

    if "email" in question:
        return handle_email_request()

    if "meeting" in question or "calendar" in question:
        return handle_calendar_request()

    if "task" in question or "focus" in question:
        return handle_task_request()

    if "know about me" in question or "memory" in question:
        return handle_memory_request()

    return "Planner Agent could not decide which specialist agent to use."