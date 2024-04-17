#!/usr/bin/python3
"""
Retrieves Records all tasks from all employees
and exports to JSON format
"""
import json
import requests


# Get the list of users
users = requests.get('https://jsonplaceholder.typicode.com/users').json()


all_tasks = {}

# Loop over all users
for user in users:

    user_id = user['id']
    user_name = user['username']

    # Get the todo list for the user
    todo_list = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}').json()

    # Create a list of dictionaries
    task_list = [{'username': user_name, 'task': task.get(
        'title'), 'completed': task.get('completed')} for task in todo_list]

    all_tasks[user_id] = task_list


with open('todo_all_employees.json', 'w') as jsonfile:
    json.dump(all_tasks, jsonfile)

if __name__ == '__main__':
    pass
