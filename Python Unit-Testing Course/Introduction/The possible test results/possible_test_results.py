import unittest


class TestPossibleResults(unittest.TestCase):
    def test_success(self):
        self.assertGreater(5, 3)

    def test_failure(self):
        self.assertGreater(3, 5)

    def test_error(self):
        self.assertGreater("five", 3)
