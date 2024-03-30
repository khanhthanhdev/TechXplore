import unittest
from unittest.mock import patch
from io import StringIO
from exercise_5 import main

class TestMain(unittest.TestCase):
    def test_1(self):
        inp = {'a': 1, 'b': 2}
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            output = mock_output.getvalue().strip()
            expected = "Khóa a có giá trị là 1\nKhóa b có giá trị là 2"
            self.assertEqual(output, expected)
    
    def test_2(self):
        inp = {'a': 1}
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            output = mock_output.getvalue().strip()
            expected = "Khóa a có giá trị là 1"
            self.assertEqual(output, expected)

    def test_3(self):
        inp = {}
        with patch("sys.stdout", new=StringIO()) as mock_output:
            main(inp)
            output = mock_output.getvalue().strip()
            expected = ""
            self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()