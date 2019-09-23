import requests
from bs4 import BeautifulSoup

from .base import ScamNumberListScraper


class ArnaquesInternetScraper(ScamNumberListScraper):
    def __init__(self):
        ScamNumberListScraper.__init__(
            self, base_url="https://assiste.com/Arnaques_telephoniques/", page_url=""
        )


def assiste(url):
    response = requests.get(url)

    page = BeautifulSoup(response.content, features="lxml")

    li_tags = page.find("ul").find_all("li")

    for li_tag in li_tags:
        if not li_tag.text.isdigit():
            continue

        a_tag = li_tag.find("a")
        print(a_tag.text)

    pass
