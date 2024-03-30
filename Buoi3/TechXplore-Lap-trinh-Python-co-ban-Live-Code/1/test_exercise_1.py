import unittest
from io import StringIO
from unittest.mock import patch
from exercise_1 import main

class TestMain(unittest.TestCase):

    def test_addition(self):
        with patch('builtins.input', side_effect=['3.5', '2.5', '+']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "6.0")

    def test_subtraction(self):
        with patch('builtins.input', side_effect=['5.8', '2.2', '-']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "3.6")

    def test_multiplication(self):
        with patch('builtins.input', side_effect=['2.5', '4.5', '*']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "11.25")

    def test_exponentiation(self):
        with patch('builtins.input', side_effect=['2', '3', '^']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "8.0")

    def test_division(self):
        with patch('builtins.input', side_effect=['10', '2', '/']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "5.0")

    def test_division_by_zero(self):
        with patch('builtins.input', side_effect=['8', '0', '/']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "Không thể chia cho 0")

    def test_invalid_operation(self):
        with patch('builtins.input', side_effect=['4', '5', '!']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "Phép tính không hợp lệ")

if __name__ == '__main__':
    unittest.main()
