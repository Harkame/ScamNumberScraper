import time

import requests
from bs4 import BeautifulSoup

DIXHUIT_URL = "http://www.dixhuit.fr"
SIGNAL_ARNAQUES_URL = (
    "https://www.signal-arnaques.com/phone-fraud?ajax=scam-table&Scam_page="
)
ARNAQUES_INTERNET_URL = (
    "http://www.arnaques-internet.info/modules.php?name=telephone&pagenum="
)


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


def signal_arnaques():
    pass


def signal_arnaques_page(page):
    response = requests.get(f"{SIGNAL_ARNAQUES_URL}{page}")

    page = BeautifulSoup(response.content, features="lxml")

    td_tags = page.find("tbody").find_all("td")

    cleared_tags = []

    for i in range(1, len(td_tags), 4):
        cleared_tags.append(td_tags[i])

    for tag in cleared_tags:
        print(tag.text)


def arnaques_internet(page):
    response = requests.get(f"{ARNAQUES_INTERNET_URL}{page}")

    page = BeautifulSoup(response.content, features="lxml")

    table = page.find("table", {"class": "table"})

    tr_tags = table.find_all("tr")

    for i in range(1, len(tr_tags)):
        b = tr_tags[i].find_all("td")[0].find("b")
        print(b.text)


if __name__ == "__main__":
    # dixhuit(1)
    # signal_arnaques_page(3)
    arnaques_internet(88)
