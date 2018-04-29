#!/usr/bin/python3
''' Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    and export the data to JSON file
'''
import json
import requests
import sys


def get_content(emp_id):
    ''' make API requests call to get todo lists and name for emp_id'''

# create urls to make requests to
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                .format(emp_id)
    user_url = "https://jsonplaceholder.typicode.com/users?id={}"\
               .format(emp_id)

# make requests
    todo_r = requests.get(todos_url)
    user_r = requests.get(user_url)

    user_json = user_r.json()
    user_name = user_json[0]['name']
    user_id = user_json[0]['id']

# create required variables
    todo_data = todo_r.json()
    file_name = "{}.json".format(emp_id)
    format_ = []
    f_dict = {}

# create the data to write to JSON file in desired format
    for item in todo_data:
        f_dict["task"] = item["title"]
        f_dict["completed"] = item["completed"]
        f_dict["username"] = user_name
        format_.append(f_dict)
    final_format = {user_id: format_}

# write the data to JSON file
    with open(file_name, 'w', encoding="utf8") as f:
        f.write(json.dumps(final_format))


if __name__ == "__main__":
    emp_id = sys.argv[1]
    get_content(emp_id)
