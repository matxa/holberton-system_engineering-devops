#!/usr/bin/python3
"""Using ReSTFull  Api to manipulate fake data
Exporting data to file in json format
"""
import json
import requests


if __name__ == "__main__":
    """dict to dict"""
    list_of_users = {}
    for i in range(1, 11):
        """request user by id"""
        request_employee = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/'.format(i))
        """json to dictionary"""
        user = json.loads(request_employee.text)
        """Get username"""
        username = user.get("username")

        """requesting all of users todo"""
        request_todos = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(i))
        """Dictionary to hold boolean value of completed tasks"""
        tasks = {}
        """json to list[dictionaries]"""
        user_todos = request_todos.json()
        """loop through all the dictionary in
        the list and get bool value of key 'completed'
        """
        for dictionary in user_todos:
            tasks.update(
                {dictionary.get("title"): dictionary.get("completed")})

        task_list = []
        for k, v in tasks.items():
            task_list.append({
                "username": username,
                "task": k,
                "completed": v,
            })
        list_of_users[i] = task_list

    """export data to file json format"""
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(list_of_users, file)
