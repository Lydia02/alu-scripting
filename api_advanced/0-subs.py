import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if not isinstance(subreddit, str):
        return 0
    
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/subuola)'}
    
    try:
        response = requests.get(url, headers=headers)
        # Check if the subreddit was not found or other client/server errors
        if response.status_code == 404 or response.status_code >= 400:
            return 0
        
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.RequestException:
        return 0
