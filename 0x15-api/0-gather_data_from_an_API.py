#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: {} employee_id'.format(argv[0]))
        exit(1)

    user_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Get the employee's information
    employee_id = requests.get(base_url + 'users/{}'.format(user_id)).json()

    # Get employee's TODO list
    todo = requests.get(base_url + 'todos', params={'userId': user_id}).json()

    # Extract the necessary information
    completed = [
            title.get("title")
            for title in todo
            if title.get('completed') is True
    ]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_id.get("name"), len(completed), len(todo)))
    [print("\t {}".format(title)) for title in completed]
