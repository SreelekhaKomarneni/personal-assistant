from tools.email_tools import get_emails
from tools.calendar_tools import get_calendar
from tools.task_tools import get_tasks
from tools.memory_tools import get_memory

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_emails",
            "description": "Get the user's emails. Can optionally filter by priority or sender.",
            "parameters": {
                "type": "object",
                "properties": {
                    "priority": {
                        "type": "string",
                        "description": "Email priority, such as high, medium, or low."
                    },
                    "sender": {
                        "type": "string",
                        "description": "Sender email address or name to filter by."
                    }
                },
                "required": []
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_calendar",
            "description": "Get the user's calendar events. Can optionally filter by date in YYYY-MM-DD format.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date to filter calendar events, in YYYY-MM-DD format."
                    }
                },
                "required": []
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_tasks",
            "description": "Get the user's tasks. Can optionally filter tasks by status.",
            "parameters": {
                "type": "object",
                "properties": {
                    "status": {
                        "type": "string",
                        "description": "Task status to filter by, such as pending or completed."
                    }
                },
                "required": []
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_memory",
            "description": "Get saved user preferences and long-term memory.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
]


available_functions = {
    "get_emails": get_emails,
    "get_calendar": get_calendar,
    "get_tasks": get_tasks,
    "get_memory": get_memory,
}