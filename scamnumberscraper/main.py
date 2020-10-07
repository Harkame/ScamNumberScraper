import time
import json
import requests
from bs4 import BeautifulSoup
import phonenumbers
from scrapers import (
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

    scraper = ArnaquesInternetScraper()
    # scraper = AssisteScraper()

    # scraper = SignalArnaquesScraper()
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

    raw_numbers = []
    invalid_numbers = []
    parsed_numbers = []

    for index in range(1, count + 1):
        page = scraper.page(index)

        for number in page:
            raw_numbers.append(number)

            try:
                parsed_number = phonenumbers.parse(number, "FR")
            except Exception:
                invalid_numbers.append(number)
                continue

            if not phonenumbers.is_valid_number(parsed_number):
                invalid_numbers.append(number)
                continue

            international_number = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164
            )

            parsed_numbers.append(international_number)

            with open("raw_arnaque_internet.json", "w") as outfile:
                json.dump(raw_numbers, outfile)

            with open("invalid_arnaque_internet.json", "w") as outfile:
                json.dump(invalid_numbers, outfile)

            with open("parsed_arnaque_internet.json", "w") as outfile:
                json.dump(parsed_numbers, outfile)

        time.sleep(10)
    # print(scraper.search("0559989827"))

    # print(scraper.list())
