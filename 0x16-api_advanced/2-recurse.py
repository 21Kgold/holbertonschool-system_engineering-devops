#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None
"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Function that returns the titles in a list of all hot articles
    """
    listing = "hot"
    url = f'https://reddit.com/r/{subreddit}/{listing}.json'
    params = {"count": count, "after": after}
    response = requests.get(url, headers={'user-agent':
                            'request'}, params=params, allow_redirects=False)
    print(response.status_code)
    if response.status_code >= 400:
        return(None)
    else:
        for element in response.json().get('data').get('children'):
            hot_list.append(element.get('data').get('title'))
        next_element = response.json().get('data').get('after')
        if not next_element:
            return (hot_list)
        else:
            return hot_list + recurse(subreddit, [],
                                      response.json().get('data').get('after'))
