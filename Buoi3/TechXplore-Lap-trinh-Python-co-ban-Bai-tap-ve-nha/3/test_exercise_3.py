import unittest
from unittest.mock import patch
from io import StringIO
from exercise_3 import main

class TestMain(unittest.TestCase):
    def test_1(self):
        inp = [1, 2, 3, 4, 5]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            output = mock_output.getvalue().strip()
            expected = "15"
            self.assertEqual(output, expected)

    def test_2(self):
        inp = [1]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            output = mock_output.getvalue().strip()
            expected = "1"
            self.assertEqual(output, expected)
    
    def test_3(self):
        inp = [1, 2]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            output = mock_output.getvalue().strip()
            expected = "3"
            self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()