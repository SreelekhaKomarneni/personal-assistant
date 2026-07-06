from agents.email_agent import handle_email_request
from agents.calendar_agent import handle_calendar_request
from agents.task_agent import handle_task_request
from agents.memory_agent import handle_memory_request


def route_request(user_question):
    question = user_question.lower()
    responses = []

    if "email" in question or "manager" in question:
        responses.append(handle_email_request())

    if "meeting" in question or "calendar" in question or "today" in question:
        responses.append(handle_calendar_request())

    if "task" in question or "focus" in question or "pending" in question:
        responses.append(handle_task_request())

    if "know about me" in question or "memory" in question or "preference" in question:
        responses.append(handle_memory_request())

    if not responses:
        return "Planner Agent could not decide which specialist agent to use."

    return "\n\n".join(responses)