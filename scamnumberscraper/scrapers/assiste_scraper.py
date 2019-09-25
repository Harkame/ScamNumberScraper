import re

import requests
from bs4 import BeautifulSoup

from .base import ScamNumberPageScraper


class AssisteScraper(ScamNumberPageScraper):
    def __init__(self):
        ScamNumberPageScraper.__init__(
            self, base_url="https://assiste.com/Arnaques_telephoniques/", page_url=""
        )

    def page(self, number):
        response = requests.get(f"{self.page_url}index_0{number}.html")

        page = BeautifulSoup(response.content, features="lxml")

        li_tags = page.find("ul").find_all("li")

        numbers = []

        for li_tag in li_tags:
            if not li_tag.text.isdigit():
                continue

            a_tag = li_tag.find("a")
            numbers.append(a_tag.text)

        return numbers

    def count(self):
        response = requests.get(
            f"https://assiste.com/Arnaques_telephoniques/index_01.html"
        )

        page = BeautifulSoup(response.content, features="lxml")

        div_tag = page.find(
            "div", {"id": "show_Dossier_Liste_Arnaques_telephoniques_et_numeros_01"}
        )

        href = div_tag.find_all("a")[-1]["href"]

        result = re.search("index_(.*).html", href)

        page = int(result.group(1))

        return page
