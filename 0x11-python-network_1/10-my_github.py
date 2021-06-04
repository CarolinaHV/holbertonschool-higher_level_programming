#!/usr/bin/python3
"""
This python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id

"""


import sys
import requests

if __name__ == "__main__":
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/user"
    resp = requests.get(url, auth=(user_name, passwd))
    try:
        print(resp.json()["id"])
    except KeyError:
        print("None")
