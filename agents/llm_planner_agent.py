import json

from services.llm_service import call_planner_llm


def create_plan(user_question):
    messages = [
        {
            "role": "system",
            "content": """
You are a planner agent.

Your job is to decide which specialist agents are needed.

Available agents:
- email_agent: use for emails, sender, priority, manager messages
- calendar_agent: use for meetings, schedule, dates, today, tomorrow
- task_agent: use for tasks, pending work, focus, priorities
- memory_agent: use for user preferences, goals, saved information

Return ONLY valid JSON in this format:

{
  "agents": [
    {
      "name": "calendar_agent",
      "arguments": {}
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

    return json.loads(content)