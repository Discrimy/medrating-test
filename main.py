import shutil
import tempfile
from datetime import datetime
from pathlib import Path

from api import fetch_users_with_tasks
from report import format_report, REPORT_DATETIME_FORMAT

OLD_REPORT_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'

if __name__ == '__main__':
    user_to_tasks = fetch_users_with_tasks()
    now = datetime.now()
    tasks_path = Path('tasks')
    tasks_path.mkdir(exist_ok=True)
    for user, tasks in user_to_tasks.items():
        report_path = tasks_path / f'{user.username}.txt'
        if report_path.exists():
            with open(report_path, mode='r', encoding='UTF-8') as report_file:
                raw_datetime = report_file.readline().strip()[-16:]
                creation_date = datetime.strptime(raw_datetime, REPORT_DATETIME_FORMAT)
            old_report_path = \
                tasks_path \
                / f'{user.username}_{creation_date.strftime(OLD_REPORT_DATETIME_FORMAT)}.txt'
            shutil.copy2(report_path, old_report_path)
        with tempfile.NamedTemporaryFile(mode='w', encoding='UTF-8', delete=False) as temp_report_file:
            temp_report_file.write(format_report(user, tasks, now))
            temp_report_name = temp_report_file.name
        shutil.move(temp_report_name, report_path)
