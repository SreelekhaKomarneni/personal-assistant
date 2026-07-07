import os
from openai import OpenAI
from tool_registry import tools
from dotenv import load_dotenv

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

def call_planner_llm(messages, latest_user_question):
    model = choose_model(latest_user_question)

    return client.chat.completions.create(
        model=model,
        messages=messages,
        response_format={"type": "json_object"}
    )