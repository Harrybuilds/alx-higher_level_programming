#!/usr/bin/python3
"""
a python script that sends a GET request to the URL
provided, along with an email address then
displays the body of the response
"""

if __name__ == '__main__':
    import requests
    import sys

    # get url passed through cli
    url = sys.argv[1]

    # send the get request
    res = requests.get(url)

    # check if HTTP status code >= 400
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        # get response body
        response = res.text
        print(response)
