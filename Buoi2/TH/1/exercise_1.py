"""
Công thức tính lãi kép ngân hàng cơ bản:
    A = P*(1 + r)^n, ^ là phép mũ
    trong đó, A là số tiền nhận được trong tương lai (kiểu dữ liệu là số thực)
            P là số tiền gốc (kiểu dữ liệu là số nguyên)
            r là lãi suất hắng năm (kiểu dữ liệu là số thực)
            n là số chu kỳ thực hiện lãi kép
            
Hãy tính số tiền 1 người có được dựa vào công thức này (làm tròn 3 chữ số thập phân sau dấu phẩy).

Để làm tròn số thập phân trong Python, có thể sử dụng hàm round của Python.
Ví dụ:
    round(1.1963, 3) = 1.196
    trong đó, 1.196 là giá trị cần làm tròn
              3 là số chữ số thập phân sau dấu phẩy

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_1.py; coverage report -m`
"""

def main():
    # TODO
    # Nhập P: số tiền gốc (số nguyên)
    p = int(input())

    # ...
    # Nhập r: lãi suất hằng năm (số thực)
    r = float(input())
    # ...
    # Nhập n: số chu kỳ thực hiện lãi kép (số nguyên)
    n = int(input())
    # Tính lãi kép
    # ...
    tong = p*(1 + r)**n
    # In ra lãi kép đã được làm tròn (chỉ cần in ra giá trị)
    # ...
    pass
    # ...
    # Tính lãi kép
    # ...
    # In ra lãi kép đã được làm tròn (chỉ cần in ra giá trị)
    print(round(tong,3))
    # ...
    pass

if __name__ == '__main__':
    main()