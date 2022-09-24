#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as r:
        html = r.read()
    print('Body response:\n',
          '\t{} type: {}\n'.format('-', type(html)),
          '\t{} content: {}\n'.format('-', html),
          '\t{} utf8 content: {}'.format('-', html.decode()))
