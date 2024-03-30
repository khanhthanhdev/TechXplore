"""
Mô tả đề bài:

Hãy viết chương trình cho phép người dùng nhập vào chiều dài và chiều rộng của 1 hình chữ nhật, sau đó tính và in ra chu vi và diện tích của hình chữ nhật có dạng như sau "<chu vi>, <diện tích>".

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_1.py; coverage report -m`
"""

def main():
    # TODO
    # Nhập vào chiều dài, chuyển đổi thành số thực
    dai = float(input())
    # Nhập vào chiều rộng, chuyển đổi thành số thực
    rong = float(input())
    # Tính chu vi   
    chuvi = (dai + rong) * 2

    # Tính diện tích
    dientich = dai * rong
    # In ra chu vi, diện tích có dạng "<chu vi>, <diện tích>"\
    print(f"{chuvi}, {dientich}")
    pass

if __name__ == '__main__':
    main()
