#!/usr/bin/python3
import json
import requests
import sys

"""
Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

employee_id = int(sys.argv[1])

"""
The script must accept an integer as a parameter, which is the employee ID
"""

employee_data = requests.get('https://jsonplaceholder.typicode.com/users/' + employee_id)
employee_data_json = employee_data.json()

"""
The script must display on the standard output the employee TODO list progress in this exact format:
"""

employee_name = employee_data_json['name']

"""
First, you have to retrieve the list of tasks of the employee
"""

todo_data = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)
todo_data_json = todo_data.json()

"""
Then, you have to display the information
"""

total_todos = str(len(todo_data_json))
completed_todos = str(sum(1 for task in todo_data_json if task ['completed']))

print("Employee " + employee_name + " is done with tasks(" +
      completed_todos + "/" + total_todos + "):")
"""
The employee name must be displayed like this: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
"""

for task in todo_data_json:
      if task['completed']:
            print('\t ' + ' ' + task['title'])

if __name__ == '__main__':
      pass
