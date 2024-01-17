import requests
import re

YOUTUBE_URL = 'https://www.youtube.com/watch?v='

def get_youtube_likes(url):
    try:
        # Send a GET request to the YouTube URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        with open('yt.html','w', encoding='utf-8') as f:
            f.write(response.text)
        
        #use a regex to extract info from json
        pattern = r'"expandedLikeCountIfLiked":{"content":"(.*?)"},'
        match = re.search(pattern, response.text)

        if match:
            # Extract the content from the match
            extracted_content = match.group(1)
            return extracted_content
        else:
            return "N/A"

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

import sys

def get_video_id():
    # Check if the video ID is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Error: Please provide the video ID as a command-line argument.")
        sys.exit(1)  # Exit the script with a non-zero status code indicating an error

    # Retrieve the video ID from the command-line argument
    video_id = sys.argv[1]

    return video_id

# Example usage
video_id = get_video_id()
video_url = YOUTUBE_URL + video_id
likes = get_youtube_likes(video_url)

print(f"Video ID {video_id} ({YOUTUBE_URL+video_id}) has {likes} likes 👍");
