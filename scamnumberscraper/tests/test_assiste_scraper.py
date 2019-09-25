import unittest

import requests

from .. import AssisteScraper


class TestAssisteScraper(unittest.TestCase):
    scraper = AssisteScraper()

    def test_count(self):
        self.assertTrue(self.scraper.count() > 0)

    def test_page(self):
        numbers = self.scraper.page(1)

        self.assertTrue(len(numbers) > 0)
