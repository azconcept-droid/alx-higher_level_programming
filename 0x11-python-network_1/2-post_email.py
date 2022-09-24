#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
displays the body of the response(decoded in utf-8)
"""
import urllib
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.
