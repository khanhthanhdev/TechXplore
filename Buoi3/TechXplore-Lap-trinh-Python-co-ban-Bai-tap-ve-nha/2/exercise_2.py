"""
# Bài tập: đếm số lượng của từng kí tự có trong 1 chuỗi.
## Mô tả đề bài:
Cho một chuỗi đã có sẵn, chương trình yêu cầu đếm số lượng của từng kí tự có trong 1 chuỗi số.

Ví dụ: 
Cho một chuỗi s = "abcxyzabbbc"
Ta thấy kí tự 'a' xuất hiện 2 lần
              'b' xuất hiện 4 lần
              'c' xuất hiện 2 lần
              'x' xuất hiện 1 lần
              'y' xuất hiện 1 lần
              'z' xuất hiện 1 lần
Chương trình cần in ra:
{'a': 2, 'b': 4, 'c': 2, 'x': 1, 'y': 1, 'z': 1} (là 1 từ điển)

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_2.py; coverage report -m`
"""

def main(s: str):
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    # TODO
    pass

if __name__ == '__main__':
    main("abcxyzabbbc")