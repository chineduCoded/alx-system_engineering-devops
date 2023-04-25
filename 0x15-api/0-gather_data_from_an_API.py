#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get("{}/{}/todos".format(base_url, employee_id))

    if response.status_code != 200:
        print("Error: Invalid employee ID")
        exit(1)

    data = response.json()
    employee_name = requests.get("{}/{}".format(
        base_url, employee_id)).json()["name"]
    total_tasks = len(data)
    completed_tasks = sum([1 for task in data if task["completed"]])
    task_titles = [task["title"] for task in data if task["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks))
    for title in task_titles:
        print("\t {}".format(title))
