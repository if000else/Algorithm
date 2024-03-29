"""
二分法分析
时间复杂度O(logn)
"""


# binary search

lis = [x for x in range(1,257)]
num = 19


def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    count = 0
    re=None
    while low <= high:
        count += 1
        mid = int((low + high) / 2)
        guess = my_list[mid]
        if item == guess:
            re=mid
            break
        if item > guess:
            low = mid + 1
        else:
            high = mid - 1
    print(re,count)


# print(lis)
binary_search(lis, 128)
