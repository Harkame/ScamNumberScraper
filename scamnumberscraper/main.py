import requests
from bs4 import BeautifulSoup

from scrapers import DixHuitScraper

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
    dixhuit_scraper = DixHuitScraper()

    # print(dixhuit_scraper.search('0699558877'))
    # print(dixhuit_scraper.search('0826270808'))

    print(dixhuit_scraper.page(42))
    print(dixhuit_scraper.page(43))

    pass
