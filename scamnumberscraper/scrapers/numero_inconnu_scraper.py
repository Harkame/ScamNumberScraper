import os

import requests
from bs4 import BeautifulSoup


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


def numero_inconnu_search(number):
    pass


class NumeroInconnuNumberComment:
    type = None
    content = None
    date = None
    like = 0
    dislike = 0

    def __init__(self):
        pass

    def __str__(self):
        to_string = "Type : "
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
