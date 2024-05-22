import unittest
from io import StringIO
from console import HBNBCommand
import sys


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Redirect stdout to capture print statements"""
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()

    def tearDown(self):
        """Reset stdout"""
        sys.stdout = self.old_stdout

    def test_quit(self):
        """Test the quit command"""
        self.assertEqual(HBNBCommand().onecmd("quit"), True)

    def test_EOF(self):
        """Test the EOF command"""
        self.assertEqual(HBNBCommand().onecmd("EOF"), True)

    def test_empty_line(self):
        """Test empty line"""
        HBNBCommand().onecmd("")
        self.assertEqual(self.mystdout.getvalue(), "")

    def test_empty_line_with_spaces(self):
        """Test empty line with spaces"""
        HBNBCommand().onecmd("    ")
        self.assertEqual(self.mystdout.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
