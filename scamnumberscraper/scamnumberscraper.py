import time

import requests
from bs4 import BeautifulSoup

DIXHUIT_URL = "http://www.dixhuit.fr"


def dixhuit(page):
    response = requests.get(f"{DIXHUIT_URL}/page/{page}")

    dixhuit_pagee = BeautifulSoup(response.content, features="lxml")

    li_tags = dixhuit_pagee.find_all("li", {"class": "page-item"})

    if len(li_tags) < 2:
        return

    next_page = li_tags[-1]

    a_tag = next_page.find("a")

    next_page = a_tag["data-ci-pagination-page"]

    dixhuit_page(next_page)

    time.sleep(1)

    dixhuit(next_page)


def dixhuit_page(page):
    response = requests.get(f"{DIXHUIT_URL}/page/{page}")

    dixhuit_page = BeautifulSoup(response.content, features="lxml")

    card_title_tags = dixhuit_page.find_all("h5", {"class": "card-title"})

    for card_title_tag in card_title_tags:
        print(card_title_tag.text)


if __name__ == "__main__":
    dixhuit(1)
