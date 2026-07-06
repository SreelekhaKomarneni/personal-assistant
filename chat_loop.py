from agents.planner_agent import route_request
from prompts import SYSTEM_PROMPT

def start_chat():
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
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

        answer = route_request(question)

        print("\nAssistant:\n")
        print(answer)
        print()