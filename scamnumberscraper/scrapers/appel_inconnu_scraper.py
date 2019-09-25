import os

import requests
from bs4 import BeautifulSoup

from .base import NotedComment, ScamNumberSearchScraper


class AppelInconnuScraper(ScamNumberSearchScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self, base_url="https://appelinconnu.fr", search_url="/numero/"
        )

    def search(self, phone_number):
        pass


class AppelInconnuNumber:
    comments = []
