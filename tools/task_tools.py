def get_tasks(status=None):
    tasks = load_json("data/tasks.json")

    if status:
        return [
            task for task in tasks
            if task.get("status", "").lower() == status.lower()
        ]

    return tasks