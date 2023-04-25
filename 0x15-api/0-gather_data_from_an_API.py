#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(base_url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [
            task.get("title")
            for task in todos
            if task.get("completed") is True
    ]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todos)))

    [print("\t {}".format(title)) for title in completed]
