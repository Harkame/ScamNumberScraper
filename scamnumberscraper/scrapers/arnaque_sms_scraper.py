import os

import requests
from bs4 import BeautifulSoup

from .base import NotedComment, ScamNumberSearchScraper


class ArnaqueSMSScraper(ScamNumberSearchScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self, base_url="https://www.arnaque-sms.com/", search_url="/"
        )

    def search(self, phone_number):
        response = requests.get(f"{self.search_url}{phone_number}.html")

        arnaque_sms_number = ArnaqueSMSNumber()

        page = BeautifulSoup(response.content, features="lxml")

        ol = page.find_all("ol")[1]

        li_tags = ol.find_all("li")

        for li in li_tags:
            arnaque_sms_number_comment = ArnaqueSMSNumberComment()

            header = li.find("dt")

            arnaque_sms_number_comment.type = header.contents[3].text

            arnaque_sms_number_comment.user = header.contents[4]

            arnaque_sms_number_comment.content = li.find("dd").text

            arnaque_sms_number_comment.date = li.find("span").text

            arnaque_sms_number.comments.append(arnaque_sms_number_comment)

        return arnaque_sms_number


class ArnaqueSMSNumber:
    comments = []


class ArnaqueSMSNumberComment:
    user = None
    type = None
    content = None
    date = None

    def __init__(self):
        pass

    def __str__(self):
        to_string = "User : "
        to_string += self.user
        to_string += os.linesep

        to_string += "Type : "
        to_string += self.type
        to_string += os.linesep

        to_string += "Content : "
        to_string += self.content
        to_string += os.linesep

        to_string += "Date : "
        to_string += self.date
        to_string += os.linesep

        return to_string
