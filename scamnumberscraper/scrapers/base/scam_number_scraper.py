from abc import ABC


class ScamNumberScraper(ABC):
    base_url = None

    def __init__(self, base_url="rgr"):
        self.base_url = base_url
