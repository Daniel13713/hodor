#!/usr/bin/python3
"""This module use request and beautifulsoup library"""

from bs4 import BeautifulSoup
import requests

URL = "http://158.69.76.135/level1.php"

with requests.session() as session:
    """With with let's keep the session open"""
    for i in range(4096):
        """We need the loop here like global to obtain
        each time the token code to vote"""

        response = session.get(URL)
        token = res.cookies["holdthedoor"]
        credentials = {"id": 3811, "holdthedoor": "submit", "key": token}

        vote = session.post(URL, data=credentials)
        print("Vote: {} -- status: {}".format(i + 1, vote.status_code))
