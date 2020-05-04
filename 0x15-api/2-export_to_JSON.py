#!/usr/bin/python3
"""This module will read the information from an API about a specific user and
export the information about their tasks into a JSON file.                  """
import json
import requests
import sys


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
    user_task_dict = {}
    json_tasks = json.loads(response_tasks.text)
    for element in json_tasks:
        if element['userId'] == int(sys.argv[1]):
            task_info = {"username": username}
            task_info["task"] = element['title']
            task_info["completed"] = element['completed']
            all_tasks_user.append(task_info)
    user_task_dict[sys.argv[1]] = all_tasks_user

    """==== Export to JSON ================================================="""
    filename = sys.argv[1] + ".json"
    with open(filename, 'w') as file:
        json.dump(user_task_dict, file)
