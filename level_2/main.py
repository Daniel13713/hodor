#!/usr/bin/python3
"""This module use request and beautifulsoup library"""


from bs4 import BeautifulSoup
import requests
import sys

is_windows = sys.platform.startswith('win')
URL = "http://158.69.76.135/level2.php"

with requests.session() as session:
    """With with let's keep the session open"""
    for i in range(1024):
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
