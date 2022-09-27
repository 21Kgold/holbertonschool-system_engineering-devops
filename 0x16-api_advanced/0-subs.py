#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given, will return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that retrieves the number of suscribers users of a given subreddit
    """
    url = "https://reddit.com/r/" + subreddit + "/about.json"
    response = requests.get(url, headers={'user-agent':
                            'holberton by claudiarpa'}).json()
    for k, v in response.items():
        if response.get('data') is None:
            return(0)
        else:
            return(response.get('data').get('subscribers'))
