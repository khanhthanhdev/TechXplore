import unittest
from io import StringIO
from unittest.mock import patch
from exercise_1 import main

class TestMain(unittest.TestCase):
    def test_1(self):
        mock_input = ["1"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "Khong phai so nguyen to")

    def test_2(self):
        mock_input = ["2"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "So nguyen to")

    def test_3(self):
        mock_input = ["3"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "So nguyen to")

    def test_4(self):
        mock_input = ["5"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "So nguyen to")

    def test_5(self):
        mock_input = ["19"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "So nguyen to")

    def test_6(self):
        mock_input = ["-1"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "Khong phai so nguyen duong")
    
    def test_7(self):
        mock_input = ["-11"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "Khong phai so nguyen duong")

    def test_8(self):
        mock_input = ["0"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "Khong phai so nguyen duong")

    def test_9(self):
        mock_input = ["100"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "Khong phai so nguyen to")

    def test_10(self):
        mock_input = ["1001"]
        with patch("builtins.input", side_effect=mock_input),\
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual(output, "Khong phai so nguyen to")

if __name__ == '__main__':
    unittest.main()