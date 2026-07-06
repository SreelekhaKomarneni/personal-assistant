from tools.task_tools import get_tasks


def handle_task_request():
    tasks = get_tasks()
    return f"Task Agent found these tasks: {tasks}"