#!/usr/bin/python3
''' Query reddit API subreddit recursively retrieve hot posts titles'''
import requests


def recurse(subreddit, hot_list=[]):
    ''' Query the subreddit recursively for hot posts'''
    url = 'https://api.reddit.com/r/{}/hot/'.format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    hot_list = query_recursively(url, hot_list, headers, subreddit)
    return hot_list


def query_recursively(url, result, headers, subreddit):
    ''' make recursive call to obtain all hot posts for a subreddit '''
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return result

    content = r.json()
    data = content['data']
    children = data['children']
    after = data['after']
    if after is None:
        return result

    for idx, item in enumerate(children):
        title = item['data']['title']
        result.append(title)

    url = 'https://api.reddit.com/r/{}/hot/?after={}'\
          .format((subreddit), after)
    result = query_recursively(url, result, headers, subreddit)
    return result
