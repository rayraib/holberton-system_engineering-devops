#!/usr/bin/python3
''' Python script that, using a REST API, for all users,
    returns information about his/her TODO list progress.
    and export the data to JSON file
'''
import json
import requests


def get_content():
    ''' make API requests call to get todo lists and name for emp_id'''

# create urls to make requests to
    user_url = "https://jsonplaceholder.typicode.com/users"

# make requests
    user_r = requests.get(user_url)

    users = user_r.json()

    file_name = "todo_all_employees.json"
    final_format = {}

# for each user in users list get their todo list
    for user in users:
        u_id = user['id']
        u_name = user['name']
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                    .format(u_id)
        todo_r = requests.get(todos_url)

        todo_data = todo_r.json()

        format_ = []
        f_dict = {}

# create the data to write to JSON file in desired format
        for item in todo_data:
            f_dict["task"] = item["title"]
            f_dict["completed"] = item["completed"]
            f_dict["username"] = u_name
            format_.append(f_dict)
        final_format[u_id] = format_

# write the data to JSON file
    with open(file_name, 'w', encoding="utf8") as f:
        f.write(json.dumps(final_format))


if __name__ == "__main__":
    get_content()
