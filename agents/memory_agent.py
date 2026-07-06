from tools.memory_tools import get_memory


def handle_memory_request():
    memory = get_memory()
    return f"Memory Agent found this memory: {memory}"