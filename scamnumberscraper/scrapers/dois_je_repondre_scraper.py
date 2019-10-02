import os

import requests
from bs4 import BeautifulSoup

from .base import Comment, NumberDetails, ScamNumberSearchScraper


class DoisJeRepondreScraper(ScamNumberSearchScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self,
            base_url="https://www.doisjerepondre.fr",
            search_url="/numero-de-telephone/0629415277",
        )

    def search(self, phone_number):
        pass


class DoisJeRepondreNumber(NumberDetails):
    pass


class DoisJeRepondreNumberComment(Comment):
    type = None
