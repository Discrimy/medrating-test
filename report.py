from datetime import datetime
from typing import List

from models import User, Task
from util import short_if_necessary

REPORT_DATETIME_FORMAT = '%d.%m.%Y %H:%M'


def format_report(user: User, tasks: List[Task], creation_datetime: datetime) -> str:
    formatted_completed_tasks = '\n'.join((short_if_necessary(task.title)
                                           for task in tasks if task.completed))
    formatted_uncompleted_tasks = '\n'.join((short_if_necessary(task.title)
                                             for task in tasks if not task.completed))

    return (
        f"{user.name} <{user.email}> {creation_datetime.strftime(REPORT_DATETIME_FORMAT)}\n"
        f"{user.company.name}\n"
        f"\n"
        f"Завершённые задачи:\n"
        f"{formatted_completed_tasks}\n"
        f"\n"
        f"Оставшиеся задачи:\n"
        f"{formatted_uncompleted_tasks}\n"
    )
