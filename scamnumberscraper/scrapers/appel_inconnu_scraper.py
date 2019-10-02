import requests
from bs4 import BeautifulSoup

from .base import NumberDetails, ScamNumberSearchScraper


class AppelInconnuScraper(ScamNumberSearchScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(self, base_url="https://appelinconnu.fr")

    def search(self, phone_number):
        response = requests.get(f"{self.base_url}/numero/{phone_number}")

        page = BeautifulSoup(response.content, features="lxml")
