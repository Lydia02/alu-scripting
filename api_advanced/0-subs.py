#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import urllib.request
import json

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or type(subreddit) != str:
        return 0
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/urllib:APIproject:v1.0.0 (by /u/username)'}
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
        return data.get("data", {}).get("subscribers", 0)
    except Exception as e:
        return 0

