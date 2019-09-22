import os

import requests
from bs4 import BeautifulSoup


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


class SignalArnaquesNumberComment:
    user = None
    content = None
    date = None
    like = 0
    dislike = 0

    def __init__(self):
        pass

    def __str__(self):
        to_string = "User : "
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
