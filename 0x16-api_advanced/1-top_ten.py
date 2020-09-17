#!/usr/bin/python3
"""
get count of subs for each each subreddit
"""
import json
import requests


def top_ten(subreddit):
    """request to get number of subs
    """
    headers = {"User-Agent": "MakingTheCheckerHappy"}

    response = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
        allow_redirects=False,
        headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        data = json_data.get('data')
        children = data.get('children')
        top_ten = children[:10]
        for post in top_ten:
            for k, v in post.items():
                if k == 'title':
                    print(v)

    print('None')
