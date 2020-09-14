#!/usr/bin/python3
"""Using ReSTFull  Api to manipulate fake data"""
import requests
from sys import argv
import json


"""request user by id"""
request_employee = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
"""json to dictionary"""
employee = json.loads(request_employee.text)
"""Get emplyee's name"""
employee_name = employee.get("name")


"""requesting all of users todo"""
request_todos = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
"""list to hold boolean value of completed tasks"""
tasks = {}
"""json to list[dictionaries]"""
employee_todos = json.loads(request_todos.text)
"""loop through all the dictionary in
the list and get bool value of key 'completed'
"""
for dictionary in employee_todos:
    tasks.update({dictionary.get("title"): dictionary.get("completed")})


"""Output name, done/total, then list done"""
EMPLOYEE_NAME = employee_name
TOTAL_NUMBER_OF_TASKS = len(tasks)
NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
print("Employee {} is done with tasks({}/{}):".format(
    EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
for k, v in tasks.items():
    if v is True:
        print('\t' + k)
