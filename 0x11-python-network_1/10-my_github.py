#!/usr/bin/python3
"""
a python script that takes your GitHub
credentials (username and password) and
uses the GitHub API to display your id
"""

if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    PAT = sys.argv[2]

    headers = {
        "Authorization": f"Bearer {PAT}"
        }

    # set url
    url = f"https://api.github.com/user"

    response = requests.get(url, headers=headers)
    user_data = response.json()
    if response.status_code == 200:
        print(user_data["id"])
    else:
        print("None")
