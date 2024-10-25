#!/usr/bin/python3
"""Print the titles of the first 10Hot Posts"""
import requests


def top_ten(subreddit):
    """The top ten titles"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"


    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            json_data = response.json()
            posts = json_data.get('data', {}).get('children', [])
            
            if posts:
                for post in posts[:10]:
                    print(post.get('data', {}).get('title'))
            else:
                print(None)
        else:
            print(None)
            
    except requests.RequestException:
        print(None)
