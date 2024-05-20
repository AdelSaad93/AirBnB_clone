import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

if __name__ == "__main__":
    unittest.main()
