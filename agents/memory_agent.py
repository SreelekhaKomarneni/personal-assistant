from tools.memory_tools import get_memory


def handle_memory_request():
    return {
        "agent": "memory_agent",
        "data": get_memory()
    }