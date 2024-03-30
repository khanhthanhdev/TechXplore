import unittest
from io import StringIO
from unittest.mock import patch
from exercise_8 import main

class TestMain(unittest.TestCase):

    def test_1(self):
        mock_input = ["abC", "Tuv"]
        
        # Sử dụng patch để giả mạo hàm input
        with patch('builtins.input', side_effect=mock_input):
            # Sử dụng StringIO để chặn việc in ra màn hình
            with patch('sys.stdout', new=StringIO()) as fake_output:
                main()  # Gọi hàm main từ main.py
                
                # Lấy giá trị đã in ra từ chương trình
                output = fake_output.getvalue().strip()
                
                # Kiểm tra xem kết quả có đúng không
                self.assertEqual(output, "vbT | Cua")  # Diện tích của hình tròn với bán kính 5 là 78.5

    def test_2(self):
        mock_input = ["xyz", "0"]
        
        # Sử dụng patch để giả mạo hàm input
        with patch('builtins.input', side_effect=mock_input):
            # Sử dụng StringIO để chặn việc in ra màn hình
            with patch('sys.stdout', new=StringIO()) as fake_output:
                main()  # Gọi hàm main từ main.py
                
                # Lấy giá trị đã in ra từ chương trình
                output = fake_output.getvalue().strip()
                
                # Kiểm tra xem kết quả có đúng không
                self.assertEqual(output, "xyz | 0")  # Diện tích của hình tròn với bán kính 5 là 78.5

if __name__ == '__main__':
    unittest.main()