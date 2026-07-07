import json
from agents.email_agent import handle_email_request
from agents.calendar_agent import handle_calendar_request
from agents.task_agent import handle_task_request
from agents.memory_agent import handle_memory_request
from services.llm_service import call_llm


def route_request(user_question):
    question = user_question.lower()
    responses = []

    if "high priority" in question and "email" in question:
        responses.append(
            handle_email_request(priority="high")
        )

    elif "email" in question or "manager" in question:
        responses.append(
            handle_email_request()
        )

    if "meeting" in question or "calendar" in question or "today" in question:
        responses.append(handle_calendar_request())

    if "pending" in question and "task" in question:
        responses.append(
            handle_task_request(status="pending")
        )

    elif "task" in question or "focus" in question:
        responses.append(
            handle_task_request()
        )

    if "know about me" in question or "memory" in question or "preference" in question:
        responses.append(handle_memory_request())

    if not responses:
        return "Planner Agent could not decide which specialist agent to use."

    combined_context = json.dumps(responses, indent=2)

    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI executive assistant. Convert specialist agent results into a clear, concise final answer."
        },
        {
            "role": "user",
            "content": f"""
    User question:
    {user_question}

    Specialist agent results:
    {combined_context}

    Give a natural final answer.
    """
        }
    ]

    llm_response = call_llm(messages, user_question)
    return llm_response.choices[0].message.content