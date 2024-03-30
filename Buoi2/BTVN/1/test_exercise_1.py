from exercise_1 import main
import unittest
from unittest.mock import patch
from io import StringIO

class TestMain(unittest.TestCase):
    def test_1(self):
        mock_input = ["3", "4"]
        with patch("builtins.input", side_effect=mock_input), \
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip().split(", ")
            self.assertEqual("14.0", output[0])
            self.assertEqual("12.0", output[1])

    def test_2(self):
        mock_input = ["5", "7"]
        with patch("builtins.input", side_effect=mock_input), \
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip().split(", ")
            self.assertEqual("24.0", output[0])
            self.assertEqual("35.0", output[1])
    
    def test_3(self):
        mock_input = ["10", "10"]
        with patch("builtins.input", side_effect=mock_input), \
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip().split(", ")
            self.assertEqual("40.0", output[0])
            self.assertEqual("100.0", output[1])

if __name__ == '__main__':
    unittest.main()