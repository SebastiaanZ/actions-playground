import unittest

from src import main


class MainTests(unittest.TestCase):
    def test_main_function(self):
        self.assertEqual(main.main(10, 20), 30)
