import os

import requests
from bs4 import BeautifulSoup

from .base import ScamNumberPageScraper, ScamNumberScraper, ScamNumberSearchScraper


class DixHuitScraper(ScamNumberSearchScraper, ScamNumberPageScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self, base_url="http://www.dixhuit.fr", search_url="/"
        )

        ScamNumberPageScraper.__init__(
            self, base_url="http://www.dixhuit.fr", page_url="/page/"
        )

    def search(self, phone_number):
        response = requests.get(f"{self.search_url}{phone_number}")

        page = BeautifulSoup(response.content, features="lxml")

        container_tags = page.find_all("div", {"class": "container"})

        if len(container_tags) == 0:
            return None

        container_1 = container_tags[1]

        spans = container_1.find_all("span")

        dixhuit_number = DixHuitNumber()

        consultations_string = spans[0].text

        dixhuit_number.consultations = consultations_string

        lis = page.find_all("li", {"class": "mb-4"})

        for li in lis:
            dixhuit_number_comment = DixHuitNumberComment()

            title_tag = li.find("h5", {"class": "mb-1"})

            dixhuit_number_comment.user = title_tag.contents[2].strip()

            date_tag = title_tag.find("meta")

            dixhuit_number_comment.date = date_tag["content"]

            body_tag = li.find("div", {"itemprop": "reviewBody"})

            dixhuit_number_comment.content = body_tag.text.strip()

            foot_tag = li.find("div", {"class": "row px-1 like_unlike"})

            spans = foot_tag.find_all("span")

            dixhuit_number_comment.like = int(spans[0].text)

            dixhuit_number_comment.like = int(spans[1].text)

            dixhuit_number.comments.append(dixhuit_number_comment)

        return dixhuit_number

    def page(self, number):
        response = requests.get(f"{self.page_url}{number}")

        dixhuit_page = BeautifulSoup(response.content, features="lxml")

        card_title_tags = dixhuit_page.find_all("h5", {"class": "card-title"})

        phones_number = []

        for card_title_tag in card_title_tags:
            phones_number.append(card_title_tag.text)

        return phones_number

    def count(self):
        response = requests.get(f"{self.base_url}")

        page = BeautifulSoup(response.content, features="lxml")

        a_tag = page.find("span", {"class": "d-none"}).find("a")

        return int(a_tag["data-ci-pagination-page"])


class DixHuitNumber:
    consultations = 0
    comments = []

    def __init__(self):
        pass

    def __str__(self):
        to_string = "Consultations : "
        to_string += self.consultations
        to_string += os.linesep

        to_string += "Comments :"

        for comment in self.comments:
            to_string += str(comment)
            to_string += os.linesep

        to_string += os.linesep

        return to_string

    def search(phone_number):
        pass


class DixHuitNumberComment:
    user = None
    date = None
    content = None
    like = 0
    dislike = 0

    def __init__(self):
        pass

    def __str__(self):
        to_string = "User : "
        to_string += self.user
        to_string += os.linesep

        to_string += "Date : "
        to_string += self.date
        to_string += os.linesep

        to_string += "Content : "
        to_string += self.content
        to_string += os.linesep

        to_string += "Like : "
        to_string += str(self.like)
        to_string += os.linesep

        to_string += "Dislike : "
        to_string += str(self.dislike)
        to_string += os.linesep

        return to_string
