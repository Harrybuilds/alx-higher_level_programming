#!/usr/bin/python3
"""
a python script that takes in a URL and an email
sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""
if __name__ == '__main__':
    import urllib.request as urlreq
    import urllib.parse as urlparse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = urlparse.urlencode({'email': email}).encode('utf-8')

    urldata = urlreq.Request(url, data=data)

    with urlreq.urlopen(urldata) as response:
        body = response.read()
        body = body.decode('utf-8')
    print(body)
