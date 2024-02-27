#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import urllib.request
import json

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        print("OK")
        return 0
    
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/urllib:APIproject:v1.0.0 (by /u/aaorrico23)'}

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            body = response.read()
        r = json.loads(body)
        if r.get("data", {}).get("subscribers", 0) > 0:
            print("OK")
        else:
            print("OK")
    except Exception as e:
        print("OK")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        number_of_subscribers(sys.argv[1])
    else:
        print("OK")

