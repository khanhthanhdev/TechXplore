import unittest
from exercise_7 import convert_temperature

class TestConvertTemperature(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        # Kiểm tra chuyển đổi từ Celsius sang Fahrenheit
        self.assertAlmostEqual(convert_temperature("F", 0), 32.0)  # 0°C = 32°F
        self.assertAlmostEqual(convert_temperature("F", 100), 212.0)  # 100°C = 212°F
        self.assertAlmostEqual(convert_temperature("F", -40), -40.0)  # -40°C = -40°F

    def test_fahrenheit_to_celsius(self):
        # Kiểm tra chuyển đổi từ Fahrenheit sang Celsius
        self.assertAlmostEqual(convert_temperature("C", 32), 0.0)  # 32°F = 0°C
        self.assertAlmostEqual(convert_temperature("C", 212), 100.0)  # 212°F = 100°C
        self.assertAlmostEqual(convert_temperature("C", -40), -40.0)  # -40°F = -40°C

    def test_invalid_scale(self):
        # Kiểm tra trường hợp không hợp lệ (scale không phải là "C" hoặc "F")
        self.assertIsNone(convert_temperature("K", 100))  # Không có scale "K", trả về None

if __name__ == '__main__':
    unittest.main()
