from tools.task_tools import get_tasks


def handle_task_request(status=None):
    return {
        "agent": "task_agent",
        "data": get_tasks(status=status)
    }