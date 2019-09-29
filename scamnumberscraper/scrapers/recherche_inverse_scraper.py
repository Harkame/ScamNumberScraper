import os

import requests
from bs4 import BeautifulSoup

from .base import NotedComment, NumberDetails, ScamNumberSearchScraper


class RechercheInverseScraper(ScamNumberSearchScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self,
            base_url="https://www.recherche-inverse.com",
            search_url="/annuaire-inverse-portable/",
        )

    def search(self, phone_number):
        pass


class RechercheInverseNumber(NumberDetails):
    pass


class RechercheInverseComment(NotedComment):
    pass
