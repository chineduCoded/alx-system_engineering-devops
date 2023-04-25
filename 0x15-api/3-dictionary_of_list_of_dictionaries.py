#!/usr/bin/python3
"""
Exports todo list of all employees to JSON format.
"""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employess = requests.get(base_url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            e.get("id"): [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": e.get("username")
            } for i in requests.get(base_url + "todos",
                                    params={"userId": e.get("id")}).json()]
            for e in employess}, jsonfile)
