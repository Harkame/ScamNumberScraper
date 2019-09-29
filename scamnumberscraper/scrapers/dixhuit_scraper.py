import os

import requests
from bs4 import BeautifulSoup

from .base import (NotedComment, NumberDetails, ScamNumberPageScraper,
                   ScamNumberSearchScraper)


class DixHuitScraper(ScamNumberSearchScraper, ScamNumberPageScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self, base_url="http://www.dixhuit.fr"
        )

        ScamNumberPageScraper.__init__(
            self, base_url="http://www.dixhuit.fr"
        )

    def search(self, phone_number):
        response = requests.get(f"{self.base_url}/{phone_number}")

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
            comment = NotedComment()

            title_tag = li.find("h5", {"class": "mb-1"})

            comment.username = title_tag.contents[2].strip()

            date_tag = title_tag.find("meta")

            comment.date = date_tag["content"]

            body_tag = li.find("div", {"itemprop": "reviewBody"})

            comment.content = body_tag.text.strip()

            foot_tag = li.find("div", {"class": "row px-1 like_unlike"})

            spans = foot_tag.find_all("span")

            comment.like = int(spans[0].text)

            comment.like = int(spans[1].text)

            dixhuit_number.comments.append(comment)

        return dixhuit_number

    def page(self, page_number):
        response = requests.get(f"{self.base_url}/page/{page_number}")

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


class DixHuitNumber(NumberDetails):
    consultations = 0

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
