#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to fetch data about an employee's TODO list progress.

It accepts an employee ID as a command-line argument and prints the employee's TODO list progress to the standard output.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Arguments:
    employee_id: An integer that represents the employee's ID.

Output:
    Prints the employee's TODO list progress in the following format:
    Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    Followed by the titles of the completed tasks, each on a new line.

Modules used:
    json: This module is used to parse the JSON data returned by the API.
    requests: This module is used to make HTTP requests to the API.
    sys: This module is used to read the command-line arguments.
"""
import json
import requests
import sys


employee_id = int(sys.argv[1])

employee_data = requests.get('https://jsonplaceholder.typicode.com/users/' + employee_id)
employee_data_json = employee_data.json()

employee_name = employee_data_json['name']

todo_data = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)
todo_data_json = todo_data.json()

total_todos = str(len(todo_data_json))
completed_todos = str(sum(1 for task in todo_data_json if task ['completed']))

print("Employee " + employee_name + " is done with tasks(" +
      completed_todos + "/" + total_todos + "):")

for task in todo_data_json:
      if task['completed']:
            print('\t ' + ' ' + task['title'])

if __name__ == '__main__':
    pass
