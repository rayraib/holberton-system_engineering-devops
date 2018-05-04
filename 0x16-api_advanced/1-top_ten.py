#!/usr/bin/python3
''' Query reddit API subreddit to retrieve top 10 hot posts titles'''
import requests


def top_ten(subreddit):
    ''' Query the subreddit for top 10 host posts'''
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0
    content = r.json()

    data = content['data']

    children = data['children']

    for idx, item in enumerate(children):
        if idx < 10:
            title = item['data']['title']
            print(title)
