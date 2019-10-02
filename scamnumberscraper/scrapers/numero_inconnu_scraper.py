import os

import requests
from bs4 import BeautifulSoup

from .base import NotedComment, ScamNumberSearchScraper


class NumeroInconnuScraper(ScamNumberSearchScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self, base_url="https://www.numeroinconnu.fr", search_url="/numero/"
        )

    def search(self, phone_number):
        pass


class NumeroInconnuNumber:
    comments = []

    def __init__(self):
        pass

    def __str__(self):
        to_string = "Comments :"

        for comment in self.comments:
            to_string += str(comment)
            to_string += os.linesep

        to_string += os.linesep

        return to_string


class NumeroInconnuNumberComment(NotedComment):
    type = None

    def __init__(self):
        pass
