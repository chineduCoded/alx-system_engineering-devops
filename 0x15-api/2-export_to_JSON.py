#!/usr/bin/python3
"""
Exports todo list for a given employee ID to JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(
            base_url + "users/{}".format(employee_id)).json()
    username = employee.get("username")
    todos = requests.get(
            base_url + "todos", params={"userId": employee_id}).json()

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username
            } for i in todos]}, jsonfile)
