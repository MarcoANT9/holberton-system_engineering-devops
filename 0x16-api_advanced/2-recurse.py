#!/usr/bin/python3
"""This Module queries the Reddit API and returns a list containing the titles
of all hot articles for a given subredit"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """This function takes a subreddit and prints its top 10 hot posts listed,
    if the subreddit is invalid, the function prints None.                 """

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if str(response) != '<Response [200]>':
        return None
    response_json = response.json()
    posts = response.json()['data']['dist'] # Number of posts on page
    index = 0
    info = response_json['data']['children'] # Dict of posts
    while index < posts:
        data = info[index]['data']['title']
        hot_list.append(data)
        index += 1
    after = response_json['data']['after']
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)


if __name__ == '__main__':
    recurse(subreddit)
