#!/usr/bin/python3
"""Gather data from an API for a given employee
ID and display TODO list progress. Export data to JSON."""
import requests
import sys
import json


def to_do(employee_ID):
    """
    Retrieve employee information and TODO
    list progress based on the employee ID.

    Args:
        employee_ID (int): The ID of the employee.

    Returns:
        None

    Prints:
        Displays the employee's TODO list progress.
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{url}/users/{employee_ID}"
    todos_url = f"{url}/todos?userId={employee_ID}"

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if employee_response.status_code == 200:
        employee_name = employee_data.get('name')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    if todos_response.status_code == 200:
        json_path = f"{employee_ID}.json"
        with open(json_path, 'w') as jsonfile:
            data = {
                "USER_ID": [
                    {
                        "task": task["title"],
                        "completed": task["completed"],
                        "username": employee_name
                    }
                    for task in todos_data
                ]
            }
            json.dump(data, jsonfile, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    to_do(employee_id)
