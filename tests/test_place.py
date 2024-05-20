import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_instance(self):
        obj = Place()
        self.assertIsInstance(obj, Place)

if __name__ == "__main__":
    unittest.main()
