#!/usr/bin/python3
"""
This script  takes in a URL, sends a request to the URL and
displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print('Error code:', res.status_code)
    else:
        print(res.text)
