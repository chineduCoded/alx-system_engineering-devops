#!/usr/bin/python3
"""Exports todo list for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(base_url + "users/{}".format(employee_id)).json()
    username = employee.get("username")
    todos = requests.get(base_url + "todos", params={"userId": employee_id}).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, username, task.get("completed"), task.get("title")]
         ) for task in todos]
