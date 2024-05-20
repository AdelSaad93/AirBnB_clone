import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_instance(self):
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

if __name__ == "__main__":
    unittest.main()
