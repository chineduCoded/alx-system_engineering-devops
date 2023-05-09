#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit.

    Args:
        subreddit (str): The subreddit to search for hot articles.
        hot_list (list): the titles of hot articles. Defaults to an empty list.
        after (str): The ID of the last post in the previous
        page of results. Defaults to None.

    Returns:
        list: the titles of all hot articles for the given subreddit,
        or None if the
        subreddit is invalid or no results are found.

    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if data is None:
        return None

    posts = data.get('children')
    if posts is None:
        return None

    for post in posts:
        hot_list.append(post.get('data').get('title'))

    after = data.get('after')
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
