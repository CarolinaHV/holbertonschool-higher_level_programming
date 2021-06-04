#!/usr/bin/python3
"""This python script fetches website"""

from urllib.request import Request, urlopen


if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    req = Request(url)
    with urlopen(req) as resp:
        site = resp.read()
        print('Body response:')
        print('\t- type: ' + str(type(site)))
        print('\t- content: ' + str(site))
        print('\t- utf8 content: ' + site.decode("utf-8"))
