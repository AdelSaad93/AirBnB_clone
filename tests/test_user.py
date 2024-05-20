import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_instance(self):
        obj = User()
        self.assertIsInstance(obj, User)

if __name__ == "__main__":
    unittest.main()
