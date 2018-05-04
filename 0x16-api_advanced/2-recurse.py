#!/usr/bin/python3
''' Query reddit API subreddit recursively retrieve hot posts titles'''
import requests


def recurse(subreddit, hot_list=[], after=""):
    ''' Query the subreddit recursively for hot posts'''

    url = 'https://api.reddit.com/r/{}/hot/?after={}'\
          .format((subreddit), after)
    headers = {
                'User-Agent': 'My User Agent 1.0'
              }

    r = requests.get(url, headers=headers, allow_redirects=False)
    # check if invalid subreddit name
    if r.status_code != 200:
        return None

    # convert and parse json data for the list of posts
    content = r.json()
    data = content['data']
    dist = data['dist']
    children = data['children']
    after = data['after']

    # call get_children that will find the title
    hot_list = get_children(hot_list, children, 0, dist)

    # if the current page it last page
    if after is None:
        return hot_list

    # construct new url with the after value to get next page
    url = 'https://api.reddit.com/r/{}/hot/?after={}'\
          .format((subreddit), after)
    hot_list = recurse(subreddit, hot_list, after)

    # if page contained no posts
    if len(hot_list) == 0:
        return None
    return hot_list


def get_children(hot_list, children, count, dist):
    ''' get the title of each hot post'''

    # retrieve title if there is content
    if count < dist:
        title = children[count]['data']['title']
        hot_list.append(title)
        count += 1
        hot_list = get_children(hot_list, children, count, dist)
        return (hot_list)
    else:
        return hot_list
