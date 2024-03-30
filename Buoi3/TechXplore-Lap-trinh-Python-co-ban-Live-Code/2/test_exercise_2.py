import unittest
from unittest.mock import patch
from io import StringIO
from exercise_2 import main

class TestMain(unittest.TestCase):
    def test_1(self):
        mock_input = ["0"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "1")
    def test_2(self):
        mock_input = ["1"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "1")
    def test_3(self):
        mock_input = ["2"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "2")
    def test_4(self):
        mock_input = ["3"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "6")
    def test_5(self):
        mock_input = ["4"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "24")
    def test_6(self):
        mock_input = ["5"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "120")
    def test_7(self):
        mock_input = ["-10"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "Khong hop le")

if __name__ == '__main__':
    unittest.main()