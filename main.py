import shutil
import tempfile
from datetime import datetime
from pathlib import Path

from api import fetch_users_with_tasks
from report import format_report
from util import REPORT_DATETIME_FORMAT, OLD_REPORT_DATETIME_FORMAT


def main():
    user_to_tasks = fetch_users_with_tasks()
    now = datetime.now()
    tasks_path = Path('tasks')
    tasks_path.mkdir(exist_ok=True)
    for user, tasks in user_to_tasks.items():
        report_path = tasks_path / f'{user.username}.txt'
        if report_path.exists():
            save_report_as_old(report_path, user)
        save_new_report(report_path, user, tasks, now)


def save_new_report(report_path, user, tasks, creation_datetime):
    with tempfile.NamedTemporaryFile(
            mode='w',
            encoding='UTF-8',
            delete=False) as temp_report_file:
        temp_report_file.write(format_report(user, tasks, creation_datetime))
        temp_report_name = temp_report_file.name
    shutil.move(temp_report_name, report_path)


def save_report_as_old(report_path, user):
    creation_date = report_creation_datetime_from_file(report_path)
    old_report_datetime_formatted = creation_date.strftime(
        OLD_REPORT_DATETIME_FORMAT)
    old_report_path = report_path.with_name(
        f'{user.username}_{old_report_datetime_formatted}.txt')
    shutil.copy2(report_path, old_report_path)


def report_creation_datetime_from_file(report_path):
    with open(report_path, mode='r', encoding='UTF-8') as report_file:
        raw_datetime = report_file.readline().strip()[-16:]
        creation_date = datetime.strptime(raw_datetime, REPORT_DATETIME_FORMAT)
    return creation_date


if __name__ == '__main__':
    main()
