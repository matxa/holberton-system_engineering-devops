#!/usr/bin/python3
"""Using ReSTFull  Api to manipulate fake data
Exporting data to file in json format
"""

if __name__ == "__main__":
    import json
    import requests

    list_of_users = {}
    for i in range(1, 11):
        request_employee = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/'.format(i))
        user = json.loads(request_employee.text)
        username = user.get("username")

        request_todos = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(i))
        tasks = {}
        user_todos = request_todos.json()
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

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(list_of_users, file)
