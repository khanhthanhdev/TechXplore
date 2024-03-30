"""
## Mô tả đề bài
Viết chương trình cho phép người dùng nhập vào lần lượt hai chuỗi s1 và s2 (có độ dài lớn hơn 1), sau đó đổi chỗ kí tự đầu tiên của chuỗi s1 và kí tự cuối cùng của chuỗi s2, đổi chỗ kí tự cuối cùng của chuỗi s1 và kí tự đầu tiên của chuỗi s2. Sau đó in ra 2 chuỗi này với định dạng là "<s1> | <s2>". Nếu một trong hai chuỗi có độ dài bé hơn bằng 1, thì chỉ in ra hai chuỗi ban đầu.

## Testcases
```
s1 = "abC"
s2 = "Tuv"
# Sau khi thực hiện đổi chỗ,thu được 2 chuỗi mới là:
s1 = "vbT", s2 = "Cua"

In ra màn hình:
vbT | Cua
```

```
s1 = "a"
s2 = "Tuv"

In ra màn hình:
a | Tuv
```

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_2.py; coverage report -m`
"""

def main():
    # TODO
    s1 = input("")
    s2 = input("")

    if len(s1) > 1 and len(s2) > 1:
        s3 = s2[-1] + s1[1:-1] + s2[0]
        s4 = s1[-1] + s2[1:-1] + s1[0]
        print(f"{s3} | {s4}")
    else:
        print(f"{s1} | {s2}")
    pass

if __name__ == '__main__':
    main()