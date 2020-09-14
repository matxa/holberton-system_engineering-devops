#!/usr/bin/python3
"""Using ReSTFull  Api to manipulate fake data
Dictionary of list of dictionaries
"""
import json
import os

if __name__ == "__main__":
    output_data = {}
    for i in range(1, 11):
        os.system('python3 2-export_to_JSON.py {}'.format(i))
        with open('{}.json'.format(i), mode='r') as file:
            data = json.load(file)
        output_data.update(data)
    with open('todo_all_employees.json', mode='w') as todo_all_employees:
        json.dump(output_data, todo_all_employees)
