"""
  - Viết chương trình cho phép người dùng nhập vào lần lượt 2 số thực a và b. Sau đó, yêu cầu người dùng nhập thêm phép tính cần thực hiện và in ra kết quả của phép tính đó.
  - Nếu phép tính là '+', in ra tổng của a và b.
  - Nếu phép tính là '-', in ra hiệu của a trừ b.
  - Nếu phép tính là '*', in ra tích của a nhân b.
  - Nếu phép tính là '^', in ra kết quả a mũ b.
  - Nếu phép tính là '/', in ra kết quả a chia b. Nếu b bằng 0, hãy in ra "Không thể chia cho 0".
  - Nếu không nằm trong các phép tính này, in ra "Phép tính không hợp lệ".

  - Lưu ý: In ra màn hình kết quả được làm tròn đến 2 chữ số thập phân sau dấu phẩy.

  Ví dụ:
  a = 1, b = 2, op = '+'
  In ra màn hình 3.00

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_1.py; coverage report -m`
"""

def main():
    a = float(input())
    b = float(input())
    op = input()
    if op == '+':
        tong = a+b
        print(round(tong,1))
    elif op == '-':
        hieu = a -b
        print(round(hieu,1))
    elif op == '*':
        tich = a*b
        print(tich)
    elif op == '^':
        mu = a**b
        print(mu)
    elif op == '/':
        if b == 0:
            print("Không thể chia cho 0")
        else:
            thuong = a/b
            print(thuong)
    else:
        print("Phép tính không hợp lệ")
    pass

if __name__ == '__main__':
    main()