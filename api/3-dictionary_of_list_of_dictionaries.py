#!/usr/bin/python3
"""Gather data from an API for all employees
and display TODO list progress. Export data to JSON."""
import json
import requests
import sys


def to_do_all_employees():
    """
    Retrieve TODO list progress for all employees.

    Returns:
        None

    Prints:
        Displays TODO list progress for all employees.
    """
    url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(url)
    users_data = users_response.json()

    if users_response.status_code == 200:
        all_employees_data = {}

        for user in users_data:
            employee_ID = user['id']
            employee_name = user['username']

            todos_url = f"{url}/{employee_ID}/todos"
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            if todos_response.status_code == 200:
                employee_tasks = []
                for task in todos_data:
                    employee_tasks.append({
                        "username": employee_name,
                        "task": task['title'],
                        "completed": task['completed']
                    })

                all_employees_data[str(employee_ID)] = employee_tasks

        json_path = 'todo_all_employees.json'
        with open(json_path, 'w') as json_file:
            json.dump(all_employees_data, json_file, indent=2)


if __name__ == "__main__":
    to_do_all_employees()
