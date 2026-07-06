from tools.task_tools import get_tasks


def handle_task_request():
    return {
        "agent": "task_agent",
        "data": get_tasks()
    }