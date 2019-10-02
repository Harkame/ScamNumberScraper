import requests
from bs4 import BeautifulSoup

from .base import (
    NotedComment,
    NumberDetails,
    ScamNumberPageScraper,
    ScamNumberSearchScraper,
)


class SignalArnaquesScraper(ScamNumberSearchScraper, ScamNumberPageScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self, base_url="https://www.signal-arnaques.com/phone-fraud"
        )

        ScamNumberPageScraper.__init__(
            self, base_url="https://www.signal-arnaques.com/phone-fraud"
        )

    def search(self, phone_number):
        response = requests.get(f"{self.base_url}?search_term={phone_number}")

        page = BeautifulSoup(response.content, features="lxml")

    def page(self, number):
        response = requests.get(f"{self.base_url}?Scam_page={number}")

        page = BeautifulSoup(response.content, features="lxml")

        tr_tags = page.find("tbody").find_all("tr")

        numbers = []

        for tr_tag in tr_tags:
            phone_number = tr_tag.find_all("td")[1].text

            numbers.append(phone_number)

        return numbers

    def count(self):
        response = requests.get(f"{self.base_url}?Scam_page=999999")

        page = BeautifulSoup(response.content, features="lxml")

        page_counter = int(
            page.find("ul", {"class": "pagination"})
            .find("li", {"class": "active"})
            .find("a")
            .text
        )

        return page_counter
