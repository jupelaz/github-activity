#!/usr/bin/env python3

import sys
import urllib.request
import json

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except urllib.error.HTTPError as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

def display_activity(events):
    for event in events:
        if event['type'] == 'PushEvent':
            repo_name = event['repo']['name']
            commit_count = len(event['payload']['commits'])
            print(f"- Pushed {commit_count} commits to {repo_name}")
        elif event['type'] == 'IssuesEvent':
            action = event['payload']['action']
            repo_name = event['repo']['name']
            print(f"- {action.capitalize()} an issue in {repo_name}")
        elif event['type'] == 'WatchEvent':
            repo_name = event['repo']['name']
            print(f"- Starred {repo_name}")
        # Add more event types as needed

def main():
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    events = fetch_github_activity(username)
    display_activity(events)

if __name__ == "__main__":
    main()