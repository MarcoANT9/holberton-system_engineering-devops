#!/usr/bin/python3
"""This module will read the information from an API about all  users and
export the information about their tasks into a JSON file.                  """
import json
import requests
import sys


if __name__ == '__main__':

    """==== Get Username =================================================="""

    url_user = "https://jsonplaceholder.typicode.com/users/"
    response_user = requests.get(url_user)
    json_user = json.loads(response_user.text)
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    response_tasks = requests.get(url_tasks)
    json_tasks = json.loads(response_tasks.text)
    user_task_dict = {}
    for user_individual in json_user:
        user_id = user_individual['id']
        username = user_individual['username']

        """==== Get User's Tasks Information =================================
            Info Needed:
                "TASK_COMPLETED_STATUS" → 'completed' in database
                "TASK_TITLE"            → 'title'     in database
        """
        all_tasks_user = []
        for element in json_tasks:
            if element['userId'] == user_id:
                task_info = {"username": username}
                task_info["task"] = element['title']
                task_info["completed"] = element['completed']
                all_tasks_user.append(task_info)
        user_task_dict[user_id] = all_tasks_user

    """==== Export to JSON ================================================="""
    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_task_dict, file)
