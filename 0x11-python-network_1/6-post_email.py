#!/usr/bin/python3
"""
a python script that sends a POST request to the URL
provided, along with an email address then
displays the body of the response
"""

if __name__ == '__main__':
    import requests
    import sys

    # get url and email passed through cli
    url = sys.argv[1]
    email = sys.argv[2]

    # Format data to be passed as a dictionary
    data = {
        'email': email
    }

    # make the post request
    res = requests.post(url, data)

    # extract the body from the data returned
    response = res.text

    print(response)
