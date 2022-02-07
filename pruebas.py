#!/usr/bin/python3
"""This module use request library"""

from bs4 import BeautifulSoup
import requests

URL = "http://158.69.76.135/level0.php"
# URL = "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"

with requests.session() as session:
    response = session.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find_all("input")
    credentials = {"id": 3811, "holdthedoor": "submit"}
    vote = session.post(URL, data=credentials)
    print(vote.status_code)

    """result_id = soup.find(id="location")
    #result_class = soup.find_all("div", class_="container")

    for container in result_class:
        titleClass = container.find("h1", class_="title")
        print(titleClass)
        print(titleClass.text)
        print(titleClass.text.strip())"""
