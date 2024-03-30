"""
## Mô tả đề bài:
Yêu cầu tìm nghiệm của phương trình bậc 2:
  a*x^2 + b*x + c = 0
trong đó a,b,c là các số thực đảm bảo phương trình luôn có 2 nghiệm phân biệt.

Để tìm căn bậc hai của một số, có thể sử dụng hàm sqrt của module math.
  Ví dụ:
    import math
    print(math.sqrt(4)) # Kết quả là 2 

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_3.py; coverage report -m`
"""

import math

def main():
    # TODO

    # Nhập a
    # ...
    # Nhập b
    # ...
    # Nhập c
    # ...
    # Tính delta
    # ...
    # Tính giá trị nghiệm x1 = (-b - căn_bậc_hai(delta))/(2a)
    # ...
    # Tính giá trị nghiệm x2 = (-b + căn_bậc_hai(delta))/(2a)
    # ...
    # In ra 2 nghiệm có dạng "<x1> <x2>"
    # ...
    a = float(input())
    b = float(input())
    c = float(input())
    delta = b**2 - 4*a*c
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    print(f"{x1} {x2}")

    pass

if __name__ == '__main__':
    main()