"""
# Bài tập: Kiểm tra số nguyên tố
## Mô tả đề bài
Viết chương trình cho phép người dùng nhập vào một số nguyên dương, sau đó kiểm tra xem số này có phải là số nguyên tố không.
- Nếu số nhập vào bé hơn hoặc bằng 0, in ra "Khong phai so nguyen duong".
- Nếu là số nguyên tố, hãy ra in "So nguyen to", ngược lại in ra "Khong phai so nguyen to".

## Lưu ý
1 không phải là số nguyên tố.

## Gợi ý
Số nguyên tố là số chia hết cho 1 và chính nó

## VÍ dụ:

```
Nhập vào số nguyên dương: 7
In ra màn hình: So nguyen to
```

```
Nhập vào số nguyên dương: 6
In ra màn hình: Khong phai so nguyen to
```

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_1.py; coverage report -m`
"""
import math
def main():
    n = int(input())
    if n <= 0:
        print("Khong phai so nguyen duong")
    elif n == 1:
        print("Khong phai so nguyen to")
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print("So nguyen to")
        else:
            print("Khong phai so nguyen to")
    # TODO
    pass

if __name__ == '__main__':
    main()