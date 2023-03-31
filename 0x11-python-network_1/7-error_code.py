#!/usr/bin/python3
"""
Python script that takes in a URL, snd request to the URL and displays the body of response(decoded in utf-8)
"""
from sys import argv
import requests

if __name__ == "__main__":
    res = requests.get(argv[1])
    try:
        res.raise_for_status()
        print(res.text)
    except requests.HTTPError:
        print(f'Error code: {res.status_code}')
