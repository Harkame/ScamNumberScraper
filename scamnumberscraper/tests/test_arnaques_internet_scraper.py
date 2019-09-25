import unittest

import requests

from .. import ArnaquesInternetScraper


class TestArnaquesInternetScraper(unittest.TestCase):
    scraper = ArnaquesInternetScraper()

    def test_count(self):
        self.assertTrue(self.scraper.count() > 0)

    def test_page(self):
        numbers = self.scraper.page(1)

        self.assertTrue(len(numbers) > 0)
