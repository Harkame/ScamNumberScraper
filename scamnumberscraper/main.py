import time
from yaml import Loader, load, dump
import json
import requests
import os
from random import randrange
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
    stream = open(config_file_path, "w+")
    dump(config, stream)


def write_array(file, array):
    with open(file, "a") as f:
        for item in array:
            print(item)
            f.write(f"{item}{os.linesep}")


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

    try:
        os.mkdir(scraper.name)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    last_number = None

    config = get_config("config.yml")

    if config is None:
        config = {}
        write_config("config.yml", config)

    if "providers" not in config:
        config = {"providers": {}}
        write_config("config.yml", config)

    provider_index = -1

    if scraper.name not in config["providers"]:
        config["providers"][scraper.name] = {"last_number": None, "last_page": 1}
        write_config("config.yml", config)

    start_index = 1

    if config["providers"][scraper.name]["last_page"] != count:
        start_index = config["providers"][scraper.name]["last_page"] + 1

    pages_progress_bar = tqdm(
        total=count,
        initial=start_index,
        bar_format="[{bar}] - [{n_fmt}/{total_fmt}] - [pages]",
    )

    for index in range(start_index, count + 1):
        raw_numbers = []
        invalid_numbers = []
        parsed_numbers = []

        page = scraper.page(index)

        for number in page:
            if last_number is None:
                last_number = number

                config = get_config("config.yml")

                config["providers"][scraper.name]["last_number"] = number

                write_config("config.yml", config)

            raw_numbers.append(number)

            try:
                parsed_number = phonenumbers.parse(number, "FR")
            except Exception:
                invalid_numbers.append(number)
                continue

            if not phonenumbers.is_valid_number(parsed_number):
                invalid_numbers.append(number)
                continue

            e164_number = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164
            )

            parsed_numbers.append(e164_number)

        with open(f"{scraper.name}/invalid.json", "w") as outfile:
            json.dump(invalid_numbers, outfile)

        write_array(f"{scraper.name}/raw.txt", raw_numbers)
        write_array(f"{scraper.name}/invalid.txt", invalid_numbers)
        write_array(f"{scraper.name}/parsed.txt", parsed_numbers)

        config["providers"][scraper.name]["last_page"] = index
        write_config("config.yml", config)

        time.sleep(randrange(30, 60))

        pages_progress_bar.update(1)

    pages_progress_bar.close()

    # print(scraper.search("0559989827"))

    # print(scraper.list())
