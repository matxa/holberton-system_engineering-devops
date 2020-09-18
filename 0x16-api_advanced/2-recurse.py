#!/usr/bin/python3
"""
get count of subs for each each subreddit
"""
import json
import requests


def recurse(subreddit, hot_list=[], counter=0):
    """request to get number of subs
    """
    headers = {"User-Agent": "MakingTheCheckerHappy"}

    response = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
        allow_redirects=False,
        headers=headers)

    list_title = []

    if response.status_code == 200:

        json_data = response.json()
        children = len(json_data.get('data').get('children'))

        if len(hot_list) <= children and counter < children:

            data = json_data.get('data').get('children')[counter]
            title = data.get('data').get('title')
            hot_list.append(title)

            list_title += recurse(subreddit, hot_list, counter+1)
        else:
            return list_title
    else:
        return None

    return hot_list
