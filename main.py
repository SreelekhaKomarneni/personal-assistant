import os
import json
from dotenv import load_dotenv
from openai import OpenAI

from agent_tools import get_emails, get_calendar, get_tasks, get_memory

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_emails",
            "description": "Get the user's emails. Can optionally filter by priority or sender.",
            "parameters": {
                "type": "object",
                "properties": {
                    "priority": {
                        "type": "string",
                        "description": "Email priority, such as high, medium, or low."
                    },
                    "sender": {
                        "type": "string",
                        "description": "Sender email address or name to filter by."
                    }
                },
                "required": []
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_calendar",
            "description": "Get the user's calendar events. Can optionally filter by date in YYYY-MM-DD format.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date to filter calendar events, in YYYY-MM-DD format."
                    }
                },
                "required": []
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_tasks",
            "description": "Get the user's tasks. Can optionally filter tasks by status.",
            "parameters": {
                "type": "object",
                "properties": {
                    "status": {
                        "type": "string",
                        "description": "Task status to filter by, such as pending or completed."
                    }
                },
                "required": []
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_memory",
            "description": "Get saved user preferences and long-term memory.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
]


available_functions = {
    "get_emails": get_emails,
    "get_calendar": get_calendar,
    "get_tasks": get_tasks,
    "get_memory": get_memory,
}

def choose_model(latest_user_question):
    question = latest_user_question.lower()

    complex_keywords = [
        "analyze",
        "prioritize",
        "strategy",
        "plan my week",
        "compare",
        "decision",
        "summarize everything"
    ]

    if any(keyword in question for keyword in complex_keywords):
        return "gpt-4.1-mini"
    
    return "gpt-4o-mini"

def call_llm(messages, latest_user_question):
    model=choose_model(latest_user_question)
    return client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools
    )

def run_agent(messages):
    latest_user_question = messages[-1]["content"]

    while True:
        response = call_llm(messages, latest_user_question)
        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        if not assistant_message.tool_calls:
            return assistant_message.content

        print("\nAgent decided to call tools:\n")

        for tool_call in assistant_message.tool_calls:
            function_name = tool_call.function.name
            print(f"Calling tool: {function_name}")

            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments or "{}")
            function_result = function_to_call(**function_args)
            print(f"Tool result: {function_result}\n")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": json.dumps(function_result)
            })


if __name__ == "__main__":
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI executive assistant. Use tools when needed."
        }
    ]

    print("AI Executive Assistant started. Type 'exit' to stop.\n")

    while True:
        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        messages.append({
            "role": "user",
            "content": question
        })

        answer = run_agent(messages)

        print("\nAssistant:\n")
        print(answer)
        print()