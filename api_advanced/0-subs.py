#!/usr/bin/python3
"""
A function that queries the Reddit API for a given subreddit
and returns the total number of subscribers.
Returns 0 if the subreddit is invalid
"""

import json
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API for a given subreddit
    and returns the total number of subscribers.
    Returns 0 if the subreddit is invalid
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyApp 0.1 (by j.dufitumuk@alustudent.com)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 302:
        return 0
    return response.json().get('data').get('subscribers')
