#!/usr/bin/python3
"""This module will read the information from an API about a specific user and
export the information about their tasks into a CSV file.                  """
import requests
import sys
import json
import csv


if __name__ == '__main__':

    """==== Get Username =================================================="""

    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_user += str(sys.argv[1])
    response_name = requests.get(url_user)
    json_user = json.loads(response_name.text)
    username = json_user['username']

    """==== Get User's Tasks Information ======================================
        Info Needed:
            "TASK_COMPLETED_STATUS" → 'completed' in database
            "TASK_TITLE"            → 'title'     in database
    """
    response_tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    all_tasks_user = []
    json_tasks = json.loads(response_tasks.text)
    for element in json_tasks:
        if element['userId'] == int(sys.argv[1]):
            task_info = [sys.argv[1], username]
            task_info.append(element['completed'])
            task_info.append(element['title'])
            all_tasks_user.append(task_info)

    """==== Export to CSV =================================================="""
    file_name = "{}.csv".format(sys.argv[1])
    with open(file_name, 'w', newline='') as csvfile:
        user_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for element in all_tasks_user:
            user_writer.writerow(element)
