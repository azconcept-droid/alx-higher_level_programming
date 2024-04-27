#!/usr/bin/python3
"""
Script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = "" if len(sys.argv) == 1 else sys.argv[1]

    letter = {'q': q}
    res = requests.post(url, letter)

    try:
        json = res.json()
        if json:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
