import unittest

import requests

from .. import FauxNumerosScraper


class TestFauxNumerosScraper(unittest.TestCase):
    scraper = FauxNumerosScraper()

    def test_list(self):
        numbers = self.scraper.list()

        assert len(numbers) > 0
