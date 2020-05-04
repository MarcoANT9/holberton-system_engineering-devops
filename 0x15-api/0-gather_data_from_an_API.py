#!/usr/bin/python3
import requests
import sys
import json


if __name__ == '__main__':

    """==== Get User Name =================================================="""

    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_user += str(sys.argv[1])
    response_name = requests.get(url_user)
    json_user = json.loads(response_name.text)
    name = json_user['name']

    """==== Get Taks for User =============================================="""

    response_tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    done_tasks = 0
    total_tasks = 0
    completed_tasks = []
    json_tasks = json.loads(response_tasks.text)
    for element in json_tasks:
        if element['userId'] == int(sys.argv[1]):
            if element['completed']:
                done_tasks += 1
                completed_tasks.append(element['title'])
            total_tasks += 1

    """==== Printing in STDOUT ============================================="""
    print("Employee {} is done with tasks({}/{}):".format(name, done_tasks,
                                                          total_tasks))
    for element in completed_tasks:
        print("\t {}".format(element))
