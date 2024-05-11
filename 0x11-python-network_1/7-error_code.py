#!/usr/bin/python3
"""
a python script that sends a GET request to the URL
provided, along with an email address then
displays the body of the response
"""

if __name__ == '__main__':
    import requests
    import sys

    # get url and email passed through cli
    url = sys.argv[1]

    try:
        # make the post request
        res = requests.get(url)

        # raise an error if status_code >= 400
        res.raise_for_status()

        # extract the body from the data returned
        response = res.text

        print(response)
    except requests.RequestException as e:
        print("Error:", e.response.status_code)
