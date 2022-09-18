#!/usr/bin/python3
"""
Script to export data in the JSON format, using a REST API
(https://jsonplaceholder.typicode.com/guide/),
Format: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS
, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed"
: TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

import json
import requests
import sys

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/users/"
    URL1 = URL + sys.argv[1]
    URL2 = URL + sys.argv[1] + "/todos"
    r1 = requests.get(URL1)
    r2 = requests.get(URL2).json()
    name = r1.json().get("name")
    total = len(r2)
    done = 0
    done_list = []
    user = r1.json().get("username")
    for task_dictionary in r2:  # r2 is a list of dictionaries
        if task_dictionary["completed"] is True:
            done = done + 1
            done_list += [task_dictionary["title"]]
    # first_line = "Employee " + name + " is done with tasks(" + str(done) + \
    #             "/" + str(total) + "):"
    # print(first_line, end="\n\t ")
    # print("\n\t " .join(done_list))
    new = [dict(zip(["task", "completed", "username"],
                    [task_dictionary["title"],
                    task_dictionary["completed"], user]))
           for task_dictionary in r2]
    new_dict = {sys.argv[1]: new}
    filename = sys.argv[1] + ".json"
    with open(filename, "w") as json_file:
        json.dump(new_dict, json_file)
