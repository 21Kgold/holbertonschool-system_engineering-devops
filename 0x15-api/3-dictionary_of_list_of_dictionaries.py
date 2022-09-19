#!/usr/bin/python3
"""
Module that, using a REST API (https://jsonplaceholder.typicode.com/guide/),
for a given employee ID (given as a second command line argument) returns
information about his/her TODO list progress.  To find object attributes:
print(request.get(URL#).json())
"""

import json
import requests
import sys

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/users/"
    new_dict = {}
    r = requests.get(URL).json()
    for id_dictionary in r:
        iD = id_dictionary["id"]
        URL2x = URL + str(iD) + "/todos"
        r2x = requests.get(URL2x).json()
        URL1x = URL + str(iD)
        r1x = requests.get(URL1x).json()
        new = [dict(zip(["task", "completed", "username"],
                    [task_dictionary["title"],
                    task_dictionary["completed"], r1x.get("username")]))
               for task_dictionary in r2x]
        new_dict[iD] = new
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(new_dict, json_file)
