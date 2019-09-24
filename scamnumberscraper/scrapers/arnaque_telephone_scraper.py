import os

import requests
from bs4 import BeautifulSoup

from .base import NotedComment, ScamNumberPageScraper, ScamNumberSearchScraper


class ArnaqueTelephoneScraper(ScamNumberSearchScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self, base_url="https://arnaque-telephone.com/", search_url="/"
        )

    def search(self, phone_number):
        pass


class ArnaqueTelephoneNumber:
    comments = []
