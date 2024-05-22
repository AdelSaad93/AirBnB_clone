import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_instance(self):
        obj = Review()
        self.assertIsInstance(obj, Review)


if __name__ == "__main__":
    unittest.main()
