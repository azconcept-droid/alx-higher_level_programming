#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
displays the body of the response(decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as r:
        print(r.read().decode('utf-8'))