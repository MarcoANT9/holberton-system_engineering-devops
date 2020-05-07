#!/usr/bin/python3
"""This Module queries the Reddit API and prints the name of the first 10 hot
post for a given subredit"""

import requests


def top_ten(subreddit):
    """This function takes a subreddit and prints its top 10 hot posts listed,
    if the subreddit is invalid, the function prints None.                 """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if str(response) != '<Response [200]>':
        print(None)
        return
    response_json = response.json()
    top_10 = 0
    info = response_json['data']['children']
    while top_10 < 10:
        data = info[top_10]['data']['title']
        print(data)
        top_10 += 1


if __name__ == '__main__':
    number_of_subscribers(subreddit)
