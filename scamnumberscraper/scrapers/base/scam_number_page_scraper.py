from abc import abstractmethod

from .scam_number_list_scraper import ScamNumberScraper


class ScamNumberPageScraper(ScamNumberScraper):
    def __init__(self, base_url="", page_url=""):
        ScamNumberScraper.__init__(self, base_url=base_url)

    @abstractmethod
    def page(self, page_number):
        raise NotImplementedError

    @abstractmethod
    def count(self):
        raise NotImplementedError
