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
                           'User-Agent': 'MyApp 0.1 (by j.dufitumuk@alustudent.com)'})

    if res.status_code != 200:
        print(None)
    else:
        json_response = res.json()
        posts = json_response.get('data').get('children')
        [print(post.get('data').get('title')) for post in posts]
