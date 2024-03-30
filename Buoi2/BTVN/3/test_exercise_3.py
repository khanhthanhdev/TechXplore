from exercise_3 import main
import unittest
from unittest.mock import patch
from io import StringIO

class TestMain(unittest.TestCase):
    def test_1(self):
        mock_input = ["1", "-3", "2"]
        with patch("builtins.input", side_effect=mock_input), \
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip().split()
            self.assertEqual("1.0", output[0])
            self.assertEqual("2.0", output[1])

    def test_2(self):
        mock_input = ["5", "7", "2"]
        with patch("builtins.input", side_effect=mock_input), \
                patch("sys.stdout", new=StringIO()) as mock_output:
            main()
            output = mock_output.getvalue().strip().split()
            self.assertEqual("-1.0", output[0])
            self.assertEqual("-0.4", output[1])

if __name__ == '__main__':
    unittest.main()