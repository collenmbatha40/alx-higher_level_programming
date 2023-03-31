#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    values = {"q": ""}

    try:
        values["q"] = argv[1]
    except IndexError:
        pass

    resp = requests.post(url, data=values)

    try:
        resp = resp.json()
        if resp == {}:
            print('No result')
        else:
            print(f"[{resp.get('id')}] {resp.get('name')}")
    except ValueError:
        print('Not a valid JSON')
