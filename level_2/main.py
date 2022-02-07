#!/usr/bin/python3
"""This module use request and beautifulsoup library"""

from bs4 import BeautifulSoup
import requests
import sys
# its win32, maybe there is win64 too?
is_windows = sys.platform.startswith('win')
URL = "http://158.69.76.135/level2.php"
print(is_windows)
with requests.session() as session:
    """With with let's keep the session open"""
    for i in range(2):
        """We need the loop here like global to obtain
        each time the token code to vote"""

        # Here we get the html of the pages
        response = session.get(URL)
        soup = BeautifulSoup(response.content, "html.parser")
        inputs = soup.find_all("input")
        for input in inputs:
            if input["name"] == "key":
                token = input["value"]
        credentials = {"id": 1, "holdthedoor": "submit", "key": token}

        if is_windows:
            vote = session.post(URL, data=credentials)
            print("Vote: {} -- status: {}".format(i + 1, vote.status_code))
