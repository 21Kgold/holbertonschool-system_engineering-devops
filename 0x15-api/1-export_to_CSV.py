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
    username = r1.json().get("username")
    new = [dict(zip(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                    "TASK_TITLE"], [int(sys.argv[1]), username,
                    task_dictionary["completed"],
                    task_dictionary["title"]])) for task_dictionary in r2]
    filename = sys.argv[1] + ".csv"
    with open(filename, "w") as my_file:
        csv_writer = csv.writer(my_file, quoting=csv.QUOTE_ALL, quotechar='"',
                                lineterminator='\n')
        for task_dictionary in new:
            csv_writer.writerow(task_dictionary.values())
