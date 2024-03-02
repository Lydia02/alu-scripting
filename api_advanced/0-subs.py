#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Fetch the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except (ValueError, KeyError):
            # In case the response does not contain the expected keys or is not valid JSON
            return 0
    else:
        # If the status code is not 200, the subreddit is likely invalid or another error occurred
        return 0
