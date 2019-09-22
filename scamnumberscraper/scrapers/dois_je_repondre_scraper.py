import os

import requests
from bs4 import BeautifulSoup


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
