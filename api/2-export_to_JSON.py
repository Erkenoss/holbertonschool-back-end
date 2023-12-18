#!/usr/bin/python3
"""Gather data from an API for a given employee
ID and display TODO list progress. Export data to JSON."""
import json
import requests
import sys


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
        total_tasks = len(todos_data)
        completed_tasks = 0
    for task in todos_data:
        completed_tasks += task['completed']

    employee_tasks = []
    for task in todos_data:
        employee_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        })

    json_path = f"{employee_ID}.json"
    with open(json_path, 'w') as json_file:
        json.dump({str(employee_ID): employee_tasks}, json_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    to_do(employee_id)
