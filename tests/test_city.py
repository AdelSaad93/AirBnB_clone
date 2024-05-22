import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_instance(self):
        obj = City()
        self.assertIsInstance(obj, City)


if __name__ == "__main__":
    unittest.main()
