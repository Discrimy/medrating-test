from typing import Dict, List

import requests

from models import User, Task

API_GATEWAY_USERS = 'https://json.medrating.org/users'
API_GATEWAY_TASKS = 'https://json.medrating.org/todos'


def fetch_users_with_tasks() -> Dict[User, List[Task]]:
    response_users = requests.get(API_GATEWAY_USERS)
    response_tasks = requests.get(API_GATEWAY_TASKS)

    user_id_to_tasks: Dict[int, List[Task]] = {}
    user_id_to_user: Dict[int, User] = {}
    for user_entry in response_users.json():
        # There are some entries with 'id' fields only
        # Ignore them
        try:
            user = User.from_dict(user_entry)
            user_id_to_tasks[user.id_] = []
            user_id_to_user[user.id_] = user
        except KeyError:
            pass

    for task_entry in response_tasks.json():
        # There are some entries with 'id' fields only
        # Ignore them
        try:
            task = Task.from_dict(task_entry)
            user_id_to_tasks[task.user_id].append(task)
        except KeyError:
            pass

    return {user_id_to_user[user_id]: tasks
            for (user_id, tasks)
            in user_id_to_tasks.items()}
