#!/usr/bin/python3
"""
a python script that sends a request to the URL
provided and displays the value of the response ID
X-Request-Id
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    with requests.get(url) as res:
        response_id = res.headers.get("X-Request-Id")

    print(response_id)
