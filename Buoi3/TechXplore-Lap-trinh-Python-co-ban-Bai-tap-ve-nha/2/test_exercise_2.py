import unittest
from unittest.mock import patch
from exercise_2 import main
from io import StringIO

class TestMain(unittest.TestCase):
    def test_1(self):
        inp = "abcxyzabbbc"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            expected = "{'a': 2, 'b': 4, 'c': 2, 'x': 1, 'y': 1, 'z': 1}"
            output = mock_output.getvalue().strip()
            self.assertEqual(output, expected)
    def test_2(self):
        inp = "aaaaaab"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            expected = "{'a': 6, 'b': 1}"
            output = mock_output.getvalue().strip()
            self.assertEqual(output, expected)
    def test_3(self):
        inp = "aaaaaa"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            expected = "{'a': 6}"
            output = mock_output.getvalue().strip()
            self.assertEqual(output, expected)
    def test_4(self):
        inp = ""
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            expected = "{}"
            output = mock_output.getvalue().strip()
            self.assertEqual(output, expected)
    def test_5(self):
        inp = "aAabB"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            expected = "{'a': 2, 'A': 1, 'b': 1, 'B': 1}"
            output = mock_output.getvalue().strip()
            self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()