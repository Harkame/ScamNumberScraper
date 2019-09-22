import requests
from bs4 import BeautifulSoup


def arnaques_internet(page):
    response = requests.get(f"{ARNAQUES_INTERNET_URL}{page}")

    page = BeautifulSoup(response.content, features="lxml")

    table = page.find("table", {"class": "table"})

    tr_tags = table.find_all("tr")

    for i in range(1, len(tr_tags)):
        b = tr_tags[i].find_all("td")[0].find("b")
        print(b.text)
