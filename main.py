import time

import requests
from bs4 import BeautifulSoup

from scamnumberscraper.scrapers import (
    AppelInconnuScraper,
    ArnaquesInternetScraper,
    ArnaqueSMSScraper,
    ArnaqueTelephoneScraper,
    AssisteScraper,
    DixHuitScraper,
    DoisJeRepondreScraper,
    FauxNumerosScraper,
    NumeroInconnuScraper,
    QuiAppeleScraper,
    RechercheInverseScraper,
    SignalArnaquesScraper,
    TellowsScraper,
)

if __name__ == "__main__":

    # scraper = FauxNumerosScraper()

    # scraper = ArnaquesInternetScraper()
    # scraper = AssisteScraper()

    scraper = SignalArnaquesScraper()
    # scraper = DixHuitScraper()

    # scraper = RechercheInverseScraper()
    # scraper = ArnaqueSMSScraper()
    # scraper = NumeroInconnuScraper()
    # scraper = DoisJeRepondreScraper()
    # scraper = TellowsScraper()
    # scraper = ArnaqueTelephoneScraper()
    # scraper = QuiAppeleScraper()
    # scraper = AppelInconnuScraper()

    count = scraper.count()

    print(count)

    for index in range(1, count + 1):
        page = scraper.page(index)
        print(page)
        time.sleep(2)
    # print(scraper.search("0559989827"))

    # print(scraper.list())
