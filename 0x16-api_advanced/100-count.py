#!/usr/bin/python3
''' Query reddit API recursively to obtain hot post titles'''
import requests
import sys


def get_children(children, word_list, word_dict, count, dist, first_call):
    ''' get the title of each hot post'''

    # retrieve title if there is content
    if count < dist:
        title = children[count]['data']['title']
        title = title.lower()
        title_list = title.split()
        if first_call is True:
            for word in word_list:
                word_dict[word] = 0
        word_dict = check_word(title_list, word_list, word_dict, 0)
        count += 1
        first_call = False
        word_dict = get_children(children, word_list,
                                 word_dict, count, dist, first_call)
        return (word_dict)
    else:
        return word_dict


def check_word(title_list, word_list, word_dict, count):
    ''' Check if one of the keyword is on a post title'''
    if count < len(word_list):
        key = word_list[count]
        if key.lower() in title_list:
            word_dict[key] += 1
        count += 1
        word_dict = check_word(title_list, word_list, word_dict, count)
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
