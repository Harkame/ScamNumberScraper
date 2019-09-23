import time

import requests
from bs4 import BeautifulSoup

from scrapers import (
    ArnaquesInternetScraper,
    ArnaqueSMSScraper,
    AssisteScraper,
    DixHuitScraper,
    DoisJeRepondreScraper,
    FauxNumerosScraper,
    NumeroInconnuScraper,
    RechercheInverseScraper,
    SignalArnaquesScraper,
)

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


if __name__ == "__main__":
    """


    print(scraper.search('0699558877'))

    """
    # scraper = DixHuitScraper()
    # scraper = ArnaquesInternetScraper()
    scraper = SignalArnaquesScraper()

    print(scraper.search("0826270808"))
    """
    for index in range(1, scraper.count()):
        print(scraper.page(index))
        time.sleep(2)
    """
