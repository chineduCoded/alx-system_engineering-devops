#!/usr/bin/python3
"""
Count words in all hot posts of a given Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Dictionary containing counts of word occurrences.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title and \
               not any((title_word in ['.', ',', '!', '?'] or title_word.endswith(('.', ',', '!', '?')))
                       for title_word in title if title_word != word.lower()):
                instances[word.lower()] = instances.get(word.lower(), 0) + title.count(word.lower())

    if after is None:
        instances = dict(sorted(instances.items(), key=lambda x: (-x[1], x[0])))
        for word, count in instances.items():
            print("{}: {}".format(word, count))
    else:
        count_words(subreddit, word_list, instances, after, count)
