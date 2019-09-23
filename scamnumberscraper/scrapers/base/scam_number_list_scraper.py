from abc import ABC, abstractmethod

from .scam_number_scraper import ScamNumberScraper


class ScamNumberListScraper(ScamNumberScraper, ABC):
    def __init__(self, base_url=""):
        ScamNumberScraper.__init__(self, base_url=base_url)

    @abstractmethod
    def list():
        raise NotImplementedError
