"""
# Bài Tập: Tìm Giá Trị Lớn Nhất trong 3 số
## Mô tả đề bài:

Hãy hiện thực hàm `max_three(a, b, c)` để tìm giá trị lớn nhất trong 3 số thực a, b, c. Giá trị trả về của hàm là số thực.

Sau đó, viết chương trình cho phép người dùng nhập vào lần lượt 3 số thực a, b, c và dùng hàm `max_three` để tìm giá trị lớn nhất và in ra giá trị lớn nhất này.

## Ví dụ:
```
Nếu người dùng nhập:
2.0
3.0
4.0

Chương trình sẽ in ra:
4.0
```

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_6.py; coverage report -m`
"""

## Hàm Tìm Giá Trị Lớn Nhất:
def max_three(a: float, b: float, c: float) -> float:
    """
    Hàm tìm giá trị lớn nhất trong 3 số thực a, b, c.

    Parameters:
    -----------
        a (float): Số thực thứ nhất.
        b (float): Số thực thứ hai.
        c (float): Số thực thứ ba.

    Returns:
    --------
        max_value (float): Giá trị lớn nhất.
    """
    if a >= b and a >= c:
        max_value = a
    elif b >= a and b >= c:
        max_value = b
    else:
        max_value = c
    print(max_value)
    # TODO
    pass

def main():
    """
    Nhập vào 3 số thực a, b, c sau đó gọi hàm max_three() để tìm số lớn nhất và in ra số này.
    """
    a,b,c = map(float, input().split())
    max_three(a, b, c)
    # TODO
    pass

if __name__ == '__main__':
    main()