#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
Print all commits by: `<sha>: <author name>` (one by line)
Use: GitHub API,
here is the documentation https://developer.github.com/v3/repos/commits/
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[2]
    repo = sys.argv[1]
    url = 'https://api.github.com/repos/' + user + '/' + repo + '/commits'
    password = 'github_pat_'
    username = 'azconcept-droid'

    res = requests.get(url, auth=(username, password))
    json = res.json()
    for i in range(0, 10):
        author = json[i]['commit']['author']['name']
        print('{}: {}'.format(json[i]['sha'], author))
