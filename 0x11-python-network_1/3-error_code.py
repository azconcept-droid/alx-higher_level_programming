#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
I manage urllib.error.HTTPError exceptions
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as r:
            response = r.read()
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
    else:
        print(response.decode('utf-8'))
