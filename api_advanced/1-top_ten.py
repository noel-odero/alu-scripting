#!/usr/bin/python3
"""Module to print the titles of the first 10 hot posts for a given subreddit"""

import requests

def top_ten(subreddit):
    """
    Fetches and prints the titles of the first 10 hot posts for a given subreddit.
    
    Parameters:
        subreddit (str): The name of the subreddit to search.

    Returns:
        None: Prints the title of each hot post if the subreddit exists.
              Prints 'None' if the subreddit is invalid or has no posts.
    """
    # Define custom headers for the request to avoid 'Too Many Requests' errors.
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    
    # Construct URL to fetch the top 10 hot posts for the given subreddit.
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    try:
        # Send GET request to Reddit API with specified URL and custom headers.
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response is successful (status code 200).
        if response.status_code == 200:
            # Parse JSON response to retrieve post data.
            json_data = response.json()
            # Extract list of posts from JSON data.
            posts = json_data.get('data', {}).get('children', [])
            
            # Check if the posts list is non-empty.
            if posts:
                # Loop through the first 10 posts and print each title.
                for post in posts[:10]:
                    print(post.get('data', {}).get('title'))
            else:
                # Print None if no posts are found.
                print(None)
        else:
            # Print None if the subreddit is invalid or does not exist.
            print(None)
            
    except requests.RequestException:
        # Print None if there was a network or request error.
        print(None)
