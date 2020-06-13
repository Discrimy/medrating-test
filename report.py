from datetime import datetime
from typing import List

from models import User, Task
from util import short_if_necessary, REPORT_DATETIME_FORMAT


def format_report(user: User, tasks: List[Task],
                  creation_datetime: datetime) -> str:
    completed_tasks_formatted = '\n'.join(
        short_if_necessary(task.title)
        for task in tasks
        if task.completed
    )
    uncompleted_tasks_formatted = '\n'.join(
        short_if_necessary(task.title)
        for task in tasks
        if not task.completed
    )
    creation_datetime_formatted = creation_datetime.strftime(
        REPORT_DATETIME_FORMAT)

    return (
        f"{user.name} <{user.email}> {creation_datetime_formatted}\n"
        f"{user.company.name}\n"
        f"\n"
        f"Завершённые задачи:\n"
        f"{completed_tasks_formatted}\n"
        f"\n"
        f"Оставшиеся задачи:\n"
        f"{uncompleted_tasks_formatted}\n"
    )
