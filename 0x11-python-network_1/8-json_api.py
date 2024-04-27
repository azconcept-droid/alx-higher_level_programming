#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
displays the body of the response(decoded in utf-8)
"""
import requests
import sys



if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
        print('No result')
    else:
        q = sys.argv[1]
        letter = {'letter': q}
        res = requests.post(url, letter)
    # with urllib.request.post(url, data={'email': sys.argv[2]}) as r:
    #     print('Your email is: {}'.format(r.getheader('email')))

# if __name__ == "__main__":
#     url = sys.argv[1]
#     email = {'email': sys.argv[2]}
#     res = requests.post(url, data=email)
#     print(res.text)