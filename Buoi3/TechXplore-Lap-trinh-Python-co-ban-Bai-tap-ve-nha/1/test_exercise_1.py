import unittest
from io import StringIO
from unittest.mock import patch
from exercise_1 import main

class TestMain(unittest.TestCase):

    def test_excellent(self):
        with patch('builtins.input', side_effect=['8']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "Gioi")

    def test_good(self):
        with patch('builtins.input', side_effect=['7']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "Kha")

    def test_average(self):
        with patch('builtins.input', side_effect=['5']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "Trung binh")

    def test_poor(self):
        with patch('builtins.input', side_effect=['3']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "Yeu")

    def test_invalid_score_1(self):
        with patch('builtins.input', side_effect=['-1.0']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "Diem khong hop le")

    def test_invalid_score_2(self):
        with patch('builtins.input', side_effect=['11']), \
             patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            result = fake_output.getvalue().strip()
            self.assertEqual(result, "Diem khong hop le")

if __name__ == '__main__':
    unittest.main()
