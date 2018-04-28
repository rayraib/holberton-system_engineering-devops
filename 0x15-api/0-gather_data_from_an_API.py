#!/usr/bin/python3
''' Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''
import requests
import sys


def get_content(emp_id):
    ''' make API requests call to get todo lists and name for emp_id'''

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                .format(emp_id)
    user_url = "https://jsonplaceholder.typicode.com/users?id={}"\
               .format(emp_id)

    todo_r = requests.get(todos_url)
    user_r = requests.get(user_url)

    todo_json = todo_r.json()
    user_json = user_r.json()

    user_name = user_json[0]['name']
    total_tasks = len(todo_json)
    comp_tasks = []

    for task in todo_json:
        if task['completed'] is True:
            comp_tasks.append(task)

    format_output(user_name, total_tasks, comp_tasks)


def format_output(user_name, total_tasks, comp_tasks):
    ''' format output to stdout'''
    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, len(comp_tasks), total_tasks))
    for task in comp_tasks:
        print("\t {}".format(task['title']))


if __name__ == "__main__":
    emp_id = sys.argv[1]
    get_content(emp_id)
