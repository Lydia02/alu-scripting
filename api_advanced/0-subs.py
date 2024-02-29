#!/usr/bin/python3
"""
Returns the number of subscribers from a subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Set a custom header user-agent."""
    headers = {"User-Agent": "ALU-scripting API 0.1"}
    url = "https://www.reddit.com/r/{}.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers,
                                timeout=30, allow_redirects=False)
    except requests.exceptions.Timeout:
        print("The request timed out.")
        return None  # Indicates that an exception occurred

    if response.status_code == 200:
        json_data = response.json()
        data_path = json_data.get("data").get("children")[0].get("data")
        subscriber_number = data_path.get("subreddit_subscribers")
        return subscriber_number
    elif response.status_code == 404:
        return 0
    else:
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = number_of_subscribers(sys.argv[1])
        if result is not None:
            print("OK")  # This will print 'OK' for both...
        else:
            print("Error executing function.")

