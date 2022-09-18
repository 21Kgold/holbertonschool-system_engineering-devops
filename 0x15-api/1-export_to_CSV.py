#!/usr/bin/python3
"""
Module that, using a REST API (https://jsonplaceholder.typicode.com/guide/),
for a given employee ID (given as a second command line argument) export data
in the CSV format. Format must be:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

import csv
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
    filename = sys.argv[1] + ".csv"
    with open(filename, "w") as my_file:
        csv_writer = csv.writer(my_file, quoting=csv.QUOTE_ALL, quotechar='"',
                                lineterminator='\n')
        for task_dictionary in r2:  # r2 is a list of dictionaries
            if task_dictionary["completed"] is True:
                done = done + 1
                done_list += [task_dictionary["title"]]
            row = [sys.argv[1], user, task_dictionary["completed"], \
                  [task_dictionary["title"]]
            csv_writer.writerow(row)
