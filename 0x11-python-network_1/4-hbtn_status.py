#!/usr/bin/python3
"""
a python script that sends a request to the URL
'https://alx-intranet.hbtn.io/status' and displays the value of
"""
if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'

    with requests.get(url) as res:
        response = res.text

    print("Body response:")
    print("\t- type:", type(response))
    print("\t- content:", response)
