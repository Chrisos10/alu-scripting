#!/usr/bin/python3
"""
check out 1-main.py to run the code
"""
import requests


def top_ten(subreddit):
    """
    A function that prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10" \
        .format(subreddit)

    res = requests.get(
            url,
            headers={
                'User-Agent': 'MyApp 0.1 (by j.dufitumuk@alustudent.com)'
                }
            )

    if res.status_code != 200:
        print(None)
    else:
        json_response = res.json()
        posts = json_response.get('data').get('children')
        [print(post.get('data').get('title')) for post in posts]
