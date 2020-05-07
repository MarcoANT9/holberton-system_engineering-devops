#!/usr/bin/python3
"""This Module queries the Reddit API and returns a list containing the titles
of all hot articles for a given subredit"""

from operator import itemgetter
import requests


def count_words(subreddit, word_list, key_list={}, after='', sorted_list=[]):
    """This function takes a subreddit and prints its top 10 hot posts listed,
    if the subreddit is invalid, the function prints None.                 """
    if key_list == {}:
        for word in word_list:
            key_list[word] = 0

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if str(response) != '<Response [200]>':
        return None

    response_json = response.json()
    posts = response.json()['data']['dist']  # Number of posts on page
    index = 0
    info = response_json['data']['children']  # Dict of posts
    while index < posts:
        data = info[index]['data']['title']
        for key in key_list:
            title = data.split(" ")
            for word in title:
                if word.lower() == key.lower():
                    key_list[key] += 1
        index += 1

    after = response_json['data']['after']
    if after is None:
        sorted_list = []
        for key in key_list:
            mini_list = (key, key_list[key])
            sorted_list.append(mini_list)
        sorted_list = sorted(sorted_list, key=itemgetter(1), reverse=True)
        for elements in sorted_list:
            if elements[1] != 0:
                print("{}: {}".format(elements[0], elements[1]))
        return
    return count_words(subreddit, word_list, key_list, after)


if __name__ == '__main__':
    count_words(subreddit, word_list)
