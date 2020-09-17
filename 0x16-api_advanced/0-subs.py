#!/usr/bin/python3
"""
get count of subs for each each subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    """request to get number of subs
    """
    headers = {"User-Agent": "MakingTheCheckerHappy"}

    response = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        allow_redirects=False,
        headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        data = json_data.get('data')
        subs = data.get('subscribers')
        return subs

    return 0
