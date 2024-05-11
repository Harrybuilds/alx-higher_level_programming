#!/usr/bin/python3
"""
python script to fetch data from 'https://alx-intranet.hbtn.io/status'
by sending a get request to that website
"""
import urllib.request as urlreq

url = 'https://alx-intranet.hbtn.io/status'

with urlreq.urlopen(url) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", utf8_content)
