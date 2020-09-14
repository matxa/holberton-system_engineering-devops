#!/usr/bin/python3
"""Using ReSTFull  Api to manipulate fake data
Exporting data to file in json format
"""
import requests
from sys import argv
import json


"""request user by id"""
request_employee = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
"""json to dictionary"""
user = json.loads(request_employee.text)
"""Get username"""
username = user.get("username")


"""requesting all of users todo"""
request_todos = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
"""Dictionary to hold boolean value of completed tasks"""
tasks = {}
"""json to list[dictionaries]"""
user_todos = json.loads(request_todos.text)
"""loop through all the dictionary in
the list and get bool value of key 'completed'
"""
for dictionary in user_todos:
    tasks.update({dictionary.get("title"): dictionary.get("completed")})

task_list = []
for k, v in tasks.items():
    task_list.append({
        "task": k,
        "completed": v,
        "username": username
    })


json_to_dump = {argv[1]: task_list}
"""export data to file json format"""
with open('{}.json'.format(argv[1]), mode='w') as file:
    json.dump(json_to_dump, file)
