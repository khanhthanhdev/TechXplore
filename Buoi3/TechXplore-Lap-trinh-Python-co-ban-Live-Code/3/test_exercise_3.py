import unittest
from unittest.mock import patch
from exercise_3 import solution_1, solution_2, solution_3
from io import StringIO

class TestMain(unittest.TestCase):
    def test_solution_1(self):
        with patch("sys.stdout", new=StringIO()) as mock_output:
            solution_1()
            output = mock_output.getvalue().strip()
            expected = "Tôi yêu DevUP"
            self.assertEqual(output, expected)
    
    def test_solution_2_1(self):
        inp = [1, 2, 3, 4, 5]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            solution_2(inp)
            output = mock_output.getvalue().strip()
            expected = "15"
            self.assertEqual(output, expected)

    def test_solution_2_2(self):
        inp = [1]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            solution_2(inp)
            output = mock_output.getvalue().strip()
            expected = "1"
            self.assertEqual(output, expected)
    
    def test_solution_2_3(self):
        inp = [1, 2]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            solution_2(inp)
            output = mock_output.getvalue().strip()
            expected = "3"
            self.assertEqual(output, expected)

    def test_solution_3_1(self):
        inp = {'a': 1, 'b': 2}
        with patch("sys.stdout", new=StringIO()) as mock_output:
            solution_3(inp)
            output = mock_output.getvalue().strip()
            expected = "Khóa a có giá trị là 1\nKhóa b có giá trị là 2"
            self.assertEqual(output, expected)
    
    def test_solution_3_2(self):
        inp = {'a': 1}
        with patch("sys.stdout", new=StringIO()) as mock_output:
            solution_3(inp)
            output = mock_output.getvalue().strip()
            expected = "Khóa a có giá trị là 1"
            self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
