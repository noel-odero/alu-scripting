#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a given subreddit"""
import requests

def top_ten(subreddit):
    """Fetches and prints the titles of the first 10 hot posts for a subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            json_data = response.json()
            posts = json_data.get('data', {}).get('children', [])
            
            # Print titles of up to 10 hot posts
            for post in posts:
                print(post.get('data', {}).get('title'))
            # If there are fewer than 10 posts
            if len(posts) == 0:
                print(None)
                
        else:
            print(None)
            
    except requests.RequestException:
        print(None)
