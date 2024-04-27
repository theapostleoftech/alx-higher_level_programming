#!/usr/bin/python3
"""
This script fetches a URL
"""
import urllib
url_to_fetch = "https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(url_to_fetch) as response:
    html = response.read()

print("Body response:")
print("-\t type: {}".format(type(html)))
print("-\t content: {}".format(html))
print("-\t utf8 content: {}".format(html.decode("utf-8")))
