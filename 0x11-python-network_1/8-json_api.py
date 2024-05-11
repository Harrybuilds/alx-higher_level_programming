#!/usr/bin/python3
"""
a python script that sends a GET request to the URL
provided, along with an email address then
displays the body of the response
"""

if __name__ == '__main__':
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # set url
    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data={"q": q})

    try:
        data = response.json()

        if data:
            print(f"[{data.id}] {data.name}")
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
