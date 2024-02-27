#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import urllib.request
import json

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/urllib:APIproject:v1.0.0 (by /u/aaorrico23)'}

    # Construct a request with custom headers
    req = urllib.request.Request(url, headers=headers)

    try:
        # Open the URL and read the response
        with urllib.request.urlopen(req) as response:
            body = response.read()
        
        # Parse the JSON response
        r = json.loads(body)
        subs = r.get("data", {}).get("subscribers", 0)
        return subs
    except Exception as e:
        print("An error occurred: {}".format(e))
        return 0

# Example usage (uncomment for testing)
# subreddit = "python"
# print(number_of_subscribers(subreddit))

