import os
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

FAUX_NUMEROS_URL = "http://fauxnumeros.fr/#fragment-14"

ASSISTE_URL = "https://assiste.com/Arnaques_telephoniques/index_01.html"

ARNAQUE_SMS = "https://www.arnaque-sms.com/"

NUMERO_INCONNU_URL = "https://www.numeroinconnu.fr/numero/"


def dixhuit_ful(page):
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


def dixhuit_search(search):
    response = requests.get(f"{DIXHUIT_URL}/{search}")

    page = BeautifulSoup(response.content, features="lxml")

    container_tags = page.find_all("div", {"class": "container"})

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


def arnaque_sms_search(number):
    response = requests.get(f"{ARNAQUE_SMS}{number}.html")

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


def numero_inconnu_search(number):
    pass


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


class ArnaqueSMSNumber:
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


class NumeroInconnuNumber:
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


class NumeroInconnuNumberComment:
    type = None
    content = None
    date = None
    like = 0
    dislike = 0

    def __init__(self):
        pass

    def __str__(self):
        to_string += "Type : "
        to_string += self.type
        to_string += os.linesep

        to_string += "Content : "
        to_string += self.content
        to_string += os.linesep

        to_string += "Date : "
        to_string += self.date
        to_string += os.linesep

        to_string += "Like : "
        to_string += int(self.like)
        to_string += os.linesep

        to_string += "Dislike : "
        to_string += int(self.dislike)
        to_string += os.linesep

        return to_string


class DoisJeRepondreNumber:
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


class DoisJeRepondreNumberComment:
    user = None
    type = None
    content = None
    date = None

    def __init__(self):
        pass

    def __str__(self):
        to_string += "User : "
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


class RechercheInverse:
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


class RechercheInverseComment:
    user = None
    content = None
    date = None
    like = 0
    dislike = 0

    def __init__(self):
        pass

    def __str__(self):
        to_string += "User : "
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
        to_string += "User : "
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


if __name__ == "__main__":
    # dixhuit_ful(1)
    # signal_arnaques_page(3)
    # arnaques_internet(88)
    # faux_numeros()
    # assiste("https://assiste.com/Arnaques_telephoniques/index_01.html")
    # assiste("https://assiste.com/Arnaques_telephoniques/index_02.html")
    # dixhuit_number = dixhuit_search("0559989827")
    # print(dixhuit_number)

    # arnaque_sms_number = arnaque_sms_search("0465414920")
    # print(arnaque_sms_number)

    pass
