#!/usr/bin/python3
"""
Module that, using a REST API (https://jsonplaceholder.typicode.com/guide/),
for a given employee ID (given as a second command line argument) returns
information about his/her TODO list progress.  To find object attributes:
print(request.get(URL#).json())
"""

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
    for task_dictionary in r2:  # r2 is a list of dictionaries
        if task_dictionary["completed"] is True:
            done = done + 1
            done_list += [task_dictionary["title"]]
    first_line = "Employee " + name + " is done with tasks(" + str(done) + \
                 "/" + str(total) + "):"
    print(first_line, end="\n\t ")
    print("\n\t " .join(done_list))
