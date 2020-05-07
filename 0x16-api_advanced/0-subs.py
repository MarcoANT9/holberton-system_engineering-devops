#!/usr/bin/python3
"""This Module queries the Reddit API and returns the number of subscribers for
a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """This function takes a subreddit and returns the number of subscribers
    if the subreddit is invalid, the function returns 0.                 """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if str(response) != '<Response [200]>':
        return 0
    response_json = response.json()
    subs = response_json.get('data').get('subscribers')
    return subs

if __name__ == '__main__':
    number_of_subscribers(subreddit)
