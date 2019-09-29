import requests
from bs4 import BeautifulSoup

from .base import ScamNumberPageScraper, ScamNumberSearchScraper


class ArnaqueTelephoneScraper(ScamNumberSearchScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self, base_url="https://arnaque-telephone.com/"
        )

    def search(self, phone_number):
        response = requests.get(f"{self.base_url}/{phone_number}.html")

        page = BeautifulSoup(response.content, features="lxml")
