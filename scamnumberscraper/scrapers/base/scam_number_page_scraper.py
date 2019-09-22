from abc import abstractmethod

from .scam_number_list_scraper import ScamNumberListScraper


class ScamNumberPageScraper(ScamNumberListScraper):
    page_url = None

    def __init__(self, base_url="", page_url=""):
        ScamNumberListScraper.__init__(self, base_url=base_url)

        self.page_url = self.base_url + page_url

    @abstractmethod
    def page(self):
        raise NotImplementedError

    @abstractmethod
    def count(self):
        raise NotImplementedError
