"""
## Mô tả đề bài
Viết chương trình cho phép người dùng nhập vào 1 số thực, đại diện điểm của 1 học sinh. Sau đó kiểm tra học lực của học sinh này dựa vào điểm đó.
  - Nếu điểm > 10 hoặc điểm < 0, in ra "Diem không hop le"
  - Nếu điểm >= 8, in ra "Gioi"
  - Nếu điểm >= 6, in ra "Kha"
  - Nếu điểm >= 4, in ra "Trung binh"
  - Ngược lại, in ra "Yeu"

## Ví dụ
```
Nhập điểm: 8
In ra màn hình: Gioi
```

```
Nhập điểm: -1.0
In ra màn hình: Diem khong hop le
```

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_1.py; coverage report -m`
"""

def main():
    n = float(input())
    if n < 0 or n > 10:
        print("Diem khong hop le")
    elif n >= 8:
        print("Gioi")
    elif n >= 6:
        print("Kha")
    elif n >= 4:
        print("Trung binh")
    else:
        print("Yeu")
    # TODO
    pass

if __name__ == '__main__':
    main()

