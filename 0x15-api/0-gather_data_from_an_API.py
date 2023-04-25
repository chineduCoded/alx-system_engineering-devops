#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""
import urllib.request
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    EMPLOYEE_ID = sys.argv[1]

    # Make request to API and load response into JSON object
    with urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(EMPLOYEE_ID)) as response:
        employee_data = json.loads(response.read().decode())

    with urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(EMPLOYEE_ID)) as response:
        todos_data = json.loads(response.read().decode())

    # Extract relevant data from JSON object
    employee_name = employee_data['name']
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])
    task_titles = [todo['title'] for todo in todos_data if todo['completed']]

    # Print results in desired format
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))
    for task_title in task_titles:
        print("\t {}".format(task_title))
