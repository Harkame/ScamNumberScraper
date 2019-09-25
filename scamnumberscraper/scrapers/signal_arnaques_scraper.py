import os

import requests
from bs4 import BeautifulSoup

from .base import ScamNumberPageScraper, ScamNumberScraper, ScamNumberSearchScraper


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

        print(f"{self.search_url}{phone_number}")

        page = BeautifulSoup(response.content, features="lxml")

    def page(self, number):
        response = requests.get(f"{self.page_url}{number}")

        page = BeautifulSoup(response.content, features="lxml")

        td_tags = page.find("tbody").find_all("td")

        numbers = []

        for i in range(1, len(td_tags), 4):
            cleared_tags.append(td_tags[i])

        return numbers

    def count(self):
        response = requests.get(f"{self.base_url}")

        page = BeautifulSoup(response.content, features="lxml")

        a_tag = page.find("span", {"class": "d-none"}).find("a")

        return int(a_tag["data-ci-pagination-page"])


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
