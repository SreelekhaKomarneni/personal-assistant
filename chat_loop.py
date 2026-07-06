from agents.personal_assistant_agent import run_agent
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

        answer = run_agent(messages)

        print("\nAssistant:\n")
        print(answer)
        print()