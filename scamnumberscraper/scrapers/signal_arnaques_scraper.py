import os

import requests
from bs4 import BeautifulSoup

from .base import ScamNumberPageScraper, ScamNumberScraper, ScamNumberSearchScraper

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


class SignalArnaquesScraper(ScamNumberSearchScraper, ScamNumberPageScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self,
            base_url="https://www.signal-arnaques.com/phone-fraud",
            search_url="?search_term=",
        )

        ScamNumberPageScraper.__init__(
            self,
            base_url="https://www.signal-arnaques.com/phone-fraud",
            page_url="?Scam_page=",
        )

    def search(self, phone_number):
        response = requests.get(f"{self.search_url}{phone_number}")

        page = BeautifulSoup(response.content, features="lxml")

    def page(self, number):
        response = requests.get(f"{self.page_url}{number}", headers=headers)

        page = BeautifulSoup(response.content, features="lxml")

        tr_tags = page.find("tbody").find_all("tr")

        numbers = []

        for tr_tag in tr_tags:
            phone_number = tr_tag.find_all("td")[1].text

            numbers.append(phone_number)

        return numbers

    def count(self):
        response = requests.get(f"{self.page_url}99999999", headers=headers)

        page = BeautifulSoup(response.content, features="lxml")
        page_counter = int(
            page.find("ul", {"class": "pagination"})
            .find("li", {"class": "active"})
            .find("a")
            .text
        )

        return page_counter


class SignalArnaquesNumber:
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


class SignalArnaquesNumberComment:
    user = None
    content = None
    date = None
    like = 0
    dislike = 0

    def __init__(self):
        pass

    def __str__(self):
        to_string = "User : "
        to_string += self.user
        to_string += os.linesep

        to_string += "Content : "
        to_string += self.content
        to_string += os.linesep

        to_string += "Date : "
        to_string += self.date
        to_string += os.linesep

        to_string += "Like : "
        to_string += str(self.like)
        to_string += os.linesep

        to_string += "Dislike : "
        to_string += str(self.dislike)
        to_string += os.linesep

        return to_string
