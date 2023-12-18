#!/usr/bin/python3
"""Gather data from an API for a given employee
ID and display TODO list progress."""
import requests
import sys
import csv


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
        employee_name = employee_data.get('username')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    if todos_response.status_code == 200:
        total_tasks = len(todos_data)
        completed_tasks = 0

        csv_path = f"{employee_ID}.csv"
        with open(csv_path, 'w', newline='') as csvfile:
            fieldnames = [
                'USER_ID',
                'USERNAME',
                'TASK_COMPLETED_STATUS',
                'TASK_TITLE'
                ]
            writer = csv.DictWriter(csvfile,
                                    fieldnames=fieldnames,
                                    quoting=csv.QUOTE_NONNUMERIC)

            for task in todos_data:
                writer.writerow({
                    'USER_ID': str(employee_ID),
                    'USERNAME': employee_name,
                    'TASK_COMPLETED_STATUS': task['completed'],
                    'TASK_TITLE': task['title']
                })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    to_do(employee_id)
