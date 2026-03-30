# Developed by:  Francisco Passos :: Frank Steps
# Developed in:  09/09/2025
# Modifield in:  03/30/2026


# import libraries to this server 
import requests
import logging
import json
import os

from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv



# Load github token on server
load_dotenv("../.env")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    # Exception: Stop server here
    raise RuntimeError("GITHUB TOKEN not found. Check your .env file.")

logging.info("Token loaded successfully!")



# Initializing flask app
app = Flask(__name__)
CORS(app)  




# This function updates the GitHub status with the YouTube video title
def update_github_status(title):
    safe_title = json.dumps(title)

    # GraphQL mutation to change GitHub user status
    query = f"""
    mutation {{
        changeUserStatus(input: {{
            emoji: ":musical_note:",
            message: {safe_title}
        }}) {{
            status {{
                emoji
                message
            }}
        }}
    }}
    """

    # Send the request to GitHub API
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.post("https://api.github.com/graphql", json={"query": query}, headers=headers)

    # Print GitHub response (for debugging)
    print("GitHub response:", response.json())




# Endpoint to receive video info from browser extension
@app.route("/video", methods=["POST"])
def video():
    data = request.json
    title = data.get("title")
    url = data.get("url")

    # Debug output in terminal
    print(f"Current video: {title}")
    print(f"URL: {url}")
    print("="*50)
    
    # Update GitHub status with the video title
    update_github_status(title)
    return "OK", 200




# Run Flask server on local machine
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
