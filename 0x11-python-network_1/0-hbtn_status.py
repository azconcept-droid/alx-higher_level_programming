#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""
import urllib


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as r:
        html = r.read()
    print('Body response:\n',
          '{} type: {}\n'.format('-', type(html)),
          '{} content: {}\n'.format('-', html),
          '{} utf8 content: {}'.format('-', r.msg))
