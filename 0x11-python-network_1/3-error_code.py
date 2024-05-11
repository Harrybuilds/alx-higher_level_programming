#!/usr/bin/python3
"""
a python script that takes in a URL and an email
sends a request to the URL and displays the value of
while also managing HTTP ERRORS
"""
if __name__ == '__main__':
    import urllib.request as request
    import urllib.error as error
    import sys

    url = sys.argv[1]

    try:
        with request.urlopen(url) as res:
            response = res.read().decode('utf-8')
            print(response)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
    """
    fetched = urlreq.urlopen(url)

    body = fetched.read().decode('utf-8')
    print(body)
    """
