#!/usr/bin/python3
"""Using ReSTFull  Api to manipulate fake data
Exporting data to file in csv format
"""
import csv
import json
import requests
from sys import argv


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


"""export data to file cvs format"""
with open('{}.csv'.format(argv[1]), mode='w') as file:
    file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
    for k, v in tasks.items():
        file_editor.writerow([argv[1], username, v, k])
