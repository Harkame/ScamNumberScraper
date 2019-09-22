import requests
from bs4 import BeautifulSoup


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
