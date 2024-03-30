import unittest
from unittest.mock import patch
from io import StringIO
from exercise_6 import max_three, main

class TestMaxThree(unittest.TestCase):
    def test_1(self):
        output = max_three(5, 3, -4)
        expected = 5
        self.assertEqual(output, expected)
    def test_2(self):
        output = max_three(5, 10, -4)
        expected = 10
        self.assertEqual(output, expected)
    def test_3(self):
        output = max_three(5, 10, 24)
        expected = 24
        self.assertEqual(output, expected)

class TestMain(unittest.TestCase):
    def test_1(self):
        mock_input = ["5", "3", "-4"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout",new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            expected = "5.0"
            self.assertEqual(output, expected)
    def test_2(self):
        mock_input = ["5", "10", "-4"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout",new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            expected = "10.0"
            self.assertEqual(output, expected)
    def test_3(self):
        mock_input = ["5", "3", "24"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout",new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            expected = "24.0"
            self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()