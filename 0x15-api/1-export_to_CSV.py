#!/usr/bin/python3
''' Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    and converts it to CSV format
'''
import csv
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

    user_json = user_r.json()

    user_name = user_json[0]['name']
    todo_data = todo_r.json()
    file_name = "{}.csv".format(emp_id)

    with open(file_name, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for user in todo_data:
            writer.writerow([user['userId'], user_name,
                            user['completed'], user['title']])


if __name__ == "__main__":
    emp_id = sys.argv[1]
    get_content(emp_id)
