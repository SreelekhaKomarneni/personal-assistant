import json

from services.llm_service import call_llm
from tool_registry import available_functions

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
