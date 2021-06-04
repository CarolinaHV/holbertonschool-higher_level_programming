#!/usr/bin/python3
"""
This python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

"""


import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    load = {"q": letter}
    resp = requests.post(url, load)
    try:
        user = resp.json()
        if (len(user) < 1):
            print("No result")
        else:
            print("[{}] {}".format(user["id"], user["name"]))
    except ValueError:
        print("Not a valid JSON")
