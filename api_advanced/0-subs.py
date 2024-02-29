#!/usr/bin/python3
"""module 0-subs.py"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Python:SubredditSubscribers:v1.0 (by /u/Lydia02)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    else:
        return 0

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscriber_count = number_of_subscribers(subreddit)
        print(f"{subscriber_count}")
