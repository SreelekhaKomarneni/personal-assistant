import json

from services.llm_service import call_planner_llm
from datetime import date, timedelta

def create_plan(user_question):
    today = date.today()
    tomorrow = today + timedelta(days=1)
    messages = [
        {
            "role": "system",
            "content": f"""
You are a planner agent.

Today's date is {today}.
Tomorrow's date is {tomorrow}.

Your job is to decide which specialist agents are needed.

Available agents:
- email_agent: use for emails, sender, priority, manager messages
- calendar_agent: use for meetings, schedule, dates, today, tomorrow
- task_agent: use for tasks, pending work, focus, priorities
- memory_agent: use for user preferences, goals, saved information

Rules:
- If user asks about meetings today, use calendar_agent with today's date.
- If user asks about meetings tomorrow, use calendar_agent with tomorrow's date.
- If user asks what to focus on today, use task_agent and calendar_agent.
- If user says "based on what you know about me", use memory_agent.
- If user asks for pending tasks, use task_agent with status "pending".

Return ONLY valid JSON in this format:

{
  "agents": [
    {
      "name": "calendar_agent",
      "arguments": {{
        "date":"{today}"
      }}
    }
  ]
}
"""
        },
        {
            "role": "user",
            "content": user_question
        }
    ]

    response = call_planner_llm(messages, user_question)
    content = response.choices[0].message.content

    if content is None:
        raise ValueError("Planner returned no text content.")

    return json.loads(content)