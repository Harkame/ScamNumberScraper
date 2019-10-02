import os

import requests
from bs4 import BeautifulSoup

from .base import NotedComment, ScamNumberSearchScraper


class QuiAppeleScraper(ScamNumberSearchScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self, base_url="https://quiappele.fr", search_url="/"
        )

    def search(self, phone_number):
        pass
