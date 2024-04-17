#!/usr/bin/python3
"""Script to export data in the JSON format"""
import json
import requests
import sys


def todo_list(employee_id):
    """
    This function will fetch the URL, user info,
    TODO list and display the employee progress
    """

    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    user_id = user_data['id']
    username = user_data['username']

    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    tasks = [{"task": todo['title'], "completed":
             todo['completed'], "username": username}
             for todo in todos_data]

    # Export data to JSON
    filename = f'{user_id}.json'
    with open(filename, 'w') as jsonfile:
        json.dump({str(user_id): tasks}, jsonfile)


if __name__ == "__main__":
    """Call the function"""

    if len(sys.argv) != 2:
        print("usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    todo_list(employee_id)
