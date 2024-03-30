"""
## Mô tả bài toán:

Bài toán: Có 2 chuỗi s1 = "Tôi yêu em" và s2 = "DevUP ươm mầm tài năng Việt". Hãy thực hiện nối chuỗi sao cho chuỗi thu được cuối cùng là "Tôi yêu DevUP".

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_3.py; coverage report -m`
"""
def main():
    """
    Bài toán: thực hiện nối chuỗi sao cho chuỗi thu được cuối cùng là "Tôi yêu DevUP" và in ra chuỗi này. Lưu ý: không dùng trick là print("Tôi yêu DevUP").
    """

    s1 = "Tôi yêu em"
    s2 = "DevUP ươm mầm tài năng Việt"
    s = s1[0:7] + ' ' + s2[0:5]
    print(s)
    # TODO
    pass

if __name__ == "__main__":
    main()
    # In ra màn hình: "Tôi yêu DevUP"