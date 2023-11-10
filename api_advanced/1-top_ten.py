#!/usr/bin/python3
"""
1-main
"""
import requests


def top_ten(subreddit):
    """
    1-main
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10" \
        .format(subreddit)

    res = requests.get(url,
                       headers={
                           'User-Agent': 'cynt user agent 1.1'})

    if res.status_code != 200:
        print(None)
    else:
        json_response = res.json()
        posts = json_response.get('data').get('children')
