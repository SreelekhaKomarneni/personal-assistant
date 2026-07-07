import json
from agents.llm_planner_agent import create_plan
from agents.email_agent import handle_email_request
from agents.calendar_agent import handle_calendar_request
from agents.task_agent import handle_task_request
from agents.memory_agent import handle_memory_request
from services.llm_service import call_llm

AGENT_MAP = {
    "email_agent": handle_email_request,
    "calendar_agent": handle_calendar_request,
    "task_agent": handle_task_request,
    "memory_agent": handle_memory_request,
}

def route_request(user_question):
    plan = create_plan(user_question)

    print("\nPlanner created this plan:\n")
    print(json.dumps(plan, indent=2))

    responses = []

    for agent_call in plan.get("agents", []):
        agent_name = agent_call["name"]
        arguments = agent_call.get("arguments", {})

        agent_function = AGENT_MAP[agent_name]
        result = agent_function(**arguments)

        responses.append(result)

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