"""
# Bài Tập: Chuyển Đổi Nhiệt Độ

## Mô tả đề bài:

Viết một hàm có thể chuyển đổi nhiệt độ từ độ Celsius (°C) sang độ Fahrenheit (°F) và ngược lại. Công thức chuyển đổi như sau:

- Chuyển từ Fahrenheit (°F) sang Celsius (°C):
    C = (F - 32)*5/9

- Chuyển từ Celsius (°C) sang Fahrenheit (°F):
    F = C*9/5 + 32

## Ví dụ:

# Ví dụ 1:
result1 = convert_temperature("F", 25)
print(result1)
# Kết quả: 77.0

# Ví dụ 2:
result2 = convert_temperature("C", 86)
print(result2)
# Kết quả: 30.0

Hãy viết mã nguồn Python để triển khai hàm `convert_temperature` theo yêu cầu của đề bài.

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_7.py; coverage report -m`
"""

def convert_temperature(scale, value):
    """
    Hàm chuyển đổi nhiệt độ giữa độ Celsius (C) và độ Fahrenheit (F).

    Parameters:
    -----------
        scale (str): 
            "C": cần chuyển sang độ Celsius.
            "F": cần chuyển sang độ Fahrenheit.
            Nếu scale không là "C" hoặc "F", hàm trả về None.

        value (float): Giá trị nhiệt độ cần chuyển đổi.

    Returns:
    --------
        float: Giá trị nhiệt độ sau khi chuyển đổi.
    """
    if scale == "C":
        value= (value - 32) * 5 / 9
    elif scale == "F":
        value= (value * 9 / 5) + 32
    else:
        return None
    return float(value)


result1 = convert_temperature("F", 25)
print(result1)
# Kết quả: 77.0