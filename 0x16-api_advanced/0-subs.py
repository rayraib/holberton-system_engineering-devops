#!/usr/bin/python3
''' Query reddit API for a given subreddit to retrieve total subscribers'''
import requests


def number_of_subscribers(subreddit):
    ''' Query the subreddit for its total subscribers '''
    url = 'https://api.reddit.com/r/{}/about'.format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0
    content = r.json()

    # content currently is dict of key, value.
    # the key 'data' contains all the subreddit info including num of subsriber
    data = content['data']

    # Retrieve the value with key 'subscribers'
    sub_num = data['subscribers']

    return sub_num
