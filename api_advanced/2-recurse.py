#!/usr/bin/python3
"""
check out 2-main.py to run the code
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    A function that returns a list containing the titles of
    all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyApp 0.1 (by j.dufitumuk@alustudent.com)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:

        return None
    posts = response.json().get('data').get('children')
    hot_list = hot_list
    for post in posts:
        hot_list.append(post['data']['title'])
    return recurse(subreddit, hot_list)
