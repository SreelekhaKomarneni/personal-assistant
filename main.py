import os
import json
from dotenv import load_dotenv
from openai import OpenAI

from tools.email_tools import get_emails
from tools.calendar_tools import get_calendar
from tools.task_tools import get_tasks
from tools.memory_tools import get_memory

from tool_registry import tools
from tool_registry import available_functions

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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