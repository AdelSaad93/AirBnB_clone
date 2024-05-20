import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_instance(self):
        obj = State()
        self.assertIsInstance(obj, State)

if __name__ == "__main__":
    unittest.main()
