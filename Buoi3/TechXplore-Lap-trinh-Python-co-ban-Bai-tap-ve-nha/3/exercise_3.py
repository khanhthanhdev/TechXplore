"""
## Mô tả bài toán:
Hãy tính tổng của tất cả các phần tử có trong 1 danh sách các số nguyên.

Khi hoàn thành xong bài làm, hãy chạy câu lệnh sau trên terminal để chạy testcase:
`coverage run test_exercise_3.py; coverage report -m`
"""

from typing import List

def main(lst: List[int]):
    """
    Bài toán: tính tổng các phần tử của 1 danh sách các số nguyên và sau đó in ra tổng này.

    Parameters:
    -----------
        lst (List[int]): danh sách các số nguyên
    """
    tong = sum(lst)
    print(tong)
    pass

if __name__ == '__main__':
    main([1, 2, 3, 4, 5])
    # In ra màn hình:
    # 15