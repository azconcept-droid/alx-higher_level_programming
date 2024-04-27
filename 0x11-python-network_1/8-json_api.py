#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
displays the body of the response(decoded in utf-8)
"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('No result')
    # print(len(sys.argv))
    # letter = sys.argv[1]
    # with urllib.request.post(url, data={'email': sys.argv[2]}) as r:
    #     print('Your email is: {}'.format(r.getheader('email')))
