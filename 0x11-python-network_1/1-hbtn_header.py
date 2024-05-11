#!/usr/bin/python3
"""
a python script that takes in a URL
sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""
if __name__ == '__main__':
    import urllib.request as urlreq
    import sys

    url = sys.argv[1]

    with urlreq.urlopen(url) as response:
        x_request = response.headers.get('X-Request-Id')
        print(x_request)
