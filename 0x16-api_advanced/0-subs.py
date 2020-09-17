#!/usr/bin/python3
"""
get count of subs for each each subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    response = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit))
    if response.status_code == 200:
        json_data = response.json()
        data = json_data.get('data')
        subs = data.get('subscribers')
        return subs
    return 0
