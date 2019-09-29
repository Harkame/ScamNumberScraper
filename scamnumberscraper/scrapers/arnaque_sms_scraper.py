import requests
from bs4 import BeautifulSoup

from .base import NotedComment, NumberDetails, ScamNumberSearchScraper


class ArnaqueSMSScraper(ScamNumberSearchScraper):
    def __init__(self):
        ScamNumberSearchScraper.__init__(
            self, base_url="https://www.arnaque-sms.com/"
        )

    def search(self, phone_number):
        response = requests.get(f"{self.base_url}/{phone_number}.html")

        page = BeautifulSoup(response.content, features="lxml")

        arnaque_sms_number = NumberDetails()

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


class ArnaqueSMSNumberComment(NotedComment):
    type = None
