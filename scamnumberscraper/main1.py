import time
from yaml import Loader, load, dump
import json
import requests
import os
from tqdm import tqdm
import errno
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


def get_config(config_file_path):
    config_stream = open(config_file_path, "r")

    config_file = load(config_stream, Loader=Loader)

    config_stream.close()

    return config_file


def write_config(config_file_path, config):
    stream = open(config_file_path, "w")
    dump(config, stream)


if __name__ == "__main__":

    # scraper = FauxNumerosScraper()

    # scraper = ArnaquesInternetScraper()
    # scraper = AssisteScraper()

    # scraper = SignalArnaquesScraper()
    scraper = DixHuitScraper()

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

    try:
        os.mkdir(scraper.name)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    pages_progress_bar = tqdm(
        total=count, position=1, bar_format="[{bar}] - [{n_fmt}/{total_fmt}] - [pages]",
    )

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

            with open(f"{scraper.name}/raw.json", "w") as outfile:
                json.dump(raw_numbers, outfile)

            with open(f"{scraper.name}/invalid.json", "w") as outfile:
                json.dump(invalid_numbers, outfile)

            with open(f"{scraper.name}/parsed.json", "w") as outfile:
                json.dump(parsed_numbers, outfile)

        time.sleep(2)

        pages_progress_bar.update(1)

    pages_progress_bar.close()

    config = get_config("config.yml")

    config["providers"][scraper.name]["last_number"] = raw_numbers[0]

    write_config("config.yml", config)

    # print(scraper.search("0559989827"))

    # print(scraper.list())
