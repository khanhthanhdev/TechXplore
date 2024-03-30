"""
## Mô tả đề bài:

Viết chương trình cho phép người dùng nhập vào 3 cạnh a, b, c (là số thực) của 1 tam giác. 

Sau đó dùng công thức tính diện tích tam giác (công thức được trình bày ở file 'area_calculation.jpg') để tính diện tích và in ra diện tích này, được làm tròn 2 chữ số thập phân sau dấu phẩy.

**Gợi ý: để làm tròn 1 số, dùng hàm round
Ví dụ: round(1.3467, 2) # Kết quả trả về là 1.35

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_2.py; coverage report -m`
"""
import math
def main():
    # TODO

    # Nhập vào độ dài cạnh a, chuyển đổi thành số thực
    a = float(input())
    # Nhập vào độ dài cạnh b, chuyển đổi thành số thực
    b = float(input())
    # Nhập vào độ dài cạnh c, chuyển đổi thành số thực
    c = float(input())
    # Sử dụng công thức tính diện tích tam giác:
    p = (a+b+c)/2
    # diện tích = căn bậc hai của (p * (p - a) * (p - b) * (p - c))
    # trong đó p = (a + b + c) / 2
    nua = math.sqrt(p * (p - a) * (p - b) * (p - c))
    # In ra diện tích tam giác đã tính được
    print(round(nua, 2))
    pass

if __name__ == '__main__':
    main()
