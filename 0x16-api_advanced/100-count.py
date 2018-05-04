#!/usr/bin/python3
''' Query reddit API recursively to obtain hot post titles'''
import requests
import sys


def count_words(subreddit, word_list, word_dict={}, after="", first_call=True):
    ''' sdf '''
    url = 'https://api.reddit.com/r/{}/hot/?after={}'\
                      .format((subreddit), after)
    headers = {
                'User-Agent': 'My User Agent 1.0'
              }
    r = requests.get(url, headers=headers, allow_redirects=False)
        # check if invalid subreddit name
    if r.status_code != 200:
        print("\n")
        return
    # convert and parse json data for the list of posts
    content = r.json()
    data = content['data']
    dist = data['dist']
    children = data['children']
    after = data['after']
    # call get_children that will find the title
    word_dict = get_children(children, word_list, word_dict, 0, dist, first_call)
    first_call = False
    # if the current page it last page
    if after is None:
        print_final(word_dict, 0, word_list, len(word_list))
        return
    
    # construct new url with the after value to get next page
    url = 'https://api.reddit.com/r/{}/hot/?after={}'\
          .format((subreddit), after)
    word_dict =  count_words(subreddit, word_list,
                             word_dict, after, first_call)
    # if page contained no posts
    if len(word_dict == 0):
        print('\n')
        return
    print_final(word_dict, 0, word_list, len(word_list))
    return

def get_children(children, word_list, word_dict, count, dist, first_call):
    ''' get the title of each hot post'''

    # retrieve title if there is content
    if count < dist:
        title = children[count]['data']['title']
        title = title.lower()
        title_list = title.split()
        '''
        if first_call is True:
            for word in word_list:
                word_dict[word] = 0
        '''
        word_dict = check_word(title_list, word_list, word_dict, 0, first_call)
        count += 1
        first_call = False
        word_dict = get_children(children, word_list,
                                 word_dict, count, dist, first_call)
        return (word_dict)
    else:
        return word_dict


def check_word(title_list, word_list, word_dict, count, first_call):
    ''' Check if one of the keyword is on a post title'''
    if first_call is True:
        for word in word_list:
            word_dict[word] = 0
    if count < len(word_list):
        key = word_list[count]
        if key.lower() in title_list:
            word_dict[key] += 1
        count += 1
        first_call = False
        word_dict = check_word(title_list, word_list, word_dict, count, first_call)
    return (word_dict)


def print_final(word_dict, count, word_list, length):
    if count < length:
        key = word_list[0]
        if key in word_dict.keys():
            value = word_dict[key]
            if value != 0:
                print("{}: {}".format(key, value))
        word_list.remove(key)
        count += 1
        print_final(word_dict, count, word_list, length)
