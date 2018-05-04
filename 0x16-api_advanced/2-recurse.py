#!/usr/bin/python3
''' Query reddit API subreddit recursively retrieve hot posts titles'''
import requests


def recurse(subreddit, hot_list=[]):
    ''' Query the subreddit recursively for hot posts'''
    url = 'https://api.reddit.com/r/{}/hot/'.format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    hot_list = query_recursively(url, hot_list, headers, subreddit)
    if len(hot_list) == 0:
        return None
    return hot_list


def query_recursively(url, hot_list, headers, subreddit):
    ''' make recursive call to obtain all hot posts for a subreddit '''
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return hot_list

    content = r.json()
    data = content['data']
    dist = data['dist']
    children = data['children']
    after = data['after']
    hot_list = get_children(hot_list, children, 0, dist)
    if after is None:
        return hot_list

    url = 'https://api.reddit.com/r/{}/hot/?after={}'\
          .format((subreddit), after)
    hot_list = query_recursively(url, hot_list, headers, subreddit)
    return hot_list


def get_children(hot_list, children, count, dist):
    ''' get the title of each hot post'''
    if count < dist:
        title = children[count]['data']['title']
        hot_list.append(title)
        count += 1
        hot_list = get_children(hot_list, children, count, dist)
        return (hot_list)
    else:
        return hot_list
