#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Function that prints top ten post of a given subreddit
    """
    listing = "hot"
    limit = 10
    url = f'https://reddit.com/r/{subreddit}/{listing}.json?limit={limit}'
    response = requests.get(url, headers={'user-agent':
                            'holberton by claudiarpa'})
    if response.status_code != 200:
        print("None")
    else:
        for element in response.json().get('data').get('children'):
            print(element.get("data").get("title"))
