from abc import ABC, abstractmethod

from .scam_number_scraper import ScamNumberScraper


class ScamNumberSearchScraper(ScamNumberScraper, ABC):
    def __init__(self, base_url="", search_url=""):
        ScamNumberScraper.__init__(self, base_url=base_url)

    @abstractmethod
    def search(phone_number):
        raise NotImplementedError
