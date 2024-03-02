#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of subscribers (all subscribers)"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    """
    subreddit_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "python:subuola:0.1 (by /u/subuola)"}
    
    try:
        response = requests.get(subreddit_url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0

