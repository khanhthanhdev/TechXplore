"""
# Bài tập: Tính giải thường bằng vòng lặp While
## Mô tả đề bài
Viết chương trình tính giai thừa của 1 số nguyên không âm n được nhập từ bàn phím. Nếu n âm, in ra "Không hợp lệ".
Giai thừa của 1 số được tính như sau: 
        n! = 1*2*3*...*(n-1)*n
```
Ví dụ:
n = 0
s = 1
In ra màn hình: 1

n = 4
s = 1*2*3*4 = 24
In ra màn hình: 24
```

## Gợi ý
Bạn có thể sử dụng một vòng lặp để tính giai thừa của số nguyên dương n. Nếu n âm, in ra thông báo "Không hợp lệ".

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_2.py; coverage report -m`
"""

def main():
    n = int(input())
    if n >= 0:
        s = 1
        while n > 0:
            s *= n
            n -= 1
        print(s)
    else:
        print("Khong hop le")
    pass

if __name__ == '__main__':
    main()