from exercise_2 import main
import unittest
from unittest.mock import patch
from io import StringIO

class TestMain(unittest.TestCase):
    def test_1(self):
        mock_input = ["3", "4", "5"]
        with patch("builtins.input", side_effect=mock_input), \
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual("6.0", output)

    def test_2(self):
        mock_input = ["5", "12", "13"]
        with patch("builtins.input", side_effect=mock_input), \
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual("30.0", output)
    
    def test_3(self):
        mock_input = ["3", "5", "7"]
        with patch("builtins.input", side_effect=mock_input), \
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip()
            self.assertEqual("6.5", output)

if __name__ == '__main__':
    unittest.main()