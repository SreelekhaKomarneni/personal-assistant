from agents.personal_assistant_agent import run_agent


def start_chat():
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