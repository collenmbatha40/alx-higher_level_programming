#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    res = response.read()
    print("Body response:")
    print(f'\t- type: {type(res)}')
    print(f'\t- content: {res}')
    print(f'\t- utf8 content: {res.decode("utf8")}')
