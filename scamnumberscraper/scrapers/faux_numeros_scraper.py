import requests
from bs4 import BeautifulSoup

from .base import ScamNumberSearchScraper


class FauxNumerosScraper(ScamNumberListScraper):
    def __init__(self):
        ScamNumberListScraper.__init__(
            self, base_url="http://fauxnumeros.fr/#fragment-14r"
        )


def faux_numeros():
    response = requests.get(f"{FAUX_NUMEROS_URL}")

    page = BeautifulSoup(response.content, features="lxml")

    p_tag = (
        page.find("div", {"id": "fragment-14"})
        .find("td", {"align": "left"})
        .find_all("p")[2]
    )

    p_tag_text = p_tag.text

    splited = p_tag_text.split("\n")

    numbers = []

    for split in splited:
        split = split.strip().replace(" ", "")

        if len(split) > 0:
            numbers.append(split[:10])

    for number in numbers:
        print(number)
