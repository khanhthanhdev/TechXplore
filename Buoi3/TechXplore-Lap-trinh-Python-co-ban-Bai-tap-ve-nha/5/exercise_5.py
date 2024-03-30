"""
## Mô tả bài toán:
Với mỗi cặp key-value của dictionary cho trước, hãy in ra nội dung sau:
    Khóa <key> có giá trị là <value>

Ví dụ cho dct = {'a': 1, 'b': 2} cần in ra các nội dung sau:
Khóa a có giá trị là 1
Khóa b có giá trị là 2

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_5.py; coverage report -m`
"""

from typing import Dict

def main(dct: Dict):
    """
    Bài toán: Với mỗi cặp key-value của dictionary cho trước, hãy in ra nội dung sau:
    Khóa <key> có giá trị là <value>

    Parameters:
    -----------
        dct (Dict): 1 từ điển
    """
    # TODO
    for i in dct.keys():
        print(f"Khóa {i} có giá trị là {dct[i]}")
    pass

if __name__ == '__main__':
    main({'a': 1, 'b': 2})
    # In ra màn hình:
    # Khóa a có giá trị là 1
    # Khóa b có giá trị là 2
