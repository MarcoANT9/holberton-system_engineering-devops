# 0x15. API

This project will cover basic aspecs of API usage.

## TASKS:

#### Task 0:
A Python script that, using a REST API, for a given employee ID, returns information about his/her TODO list progress.

Specifications:

    requests module is used.
    The script accepts an integer as a parameter, which is the employee ID
    The script displays on the standard output the employee TODO list progress in this exact format:
        First line: "Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):"
            EMPLOYEE_NAME: name of the employee
            NUMBER_OF_DONE_TASKS: number of completed tasks
            TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
        Second and N next lines display the title of completed tasks: Tab TASK_TITLE (with 1 tabulation + 1 space before)

#### Task 1:
Using the task #0, this script is used to export data in the CSV format.

Specifications:

    Records all tasks that are owned by the selected employee
    Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name: USER_ID.csv

#### Task 2:
Using the task #0, this script is used to export data in the JSON format.

Specifications:

    Records all tasks that are owned by the selected employee
    Format: { "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}
    File name: USER_ID.json

#### Task 3:
Using the task #0, this script is used to export data in the JSON format.

Specifications:

    Records all tasks from all employees
    Format: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name: todo_all_employees.json
