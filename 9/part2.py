"""
File: part2.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: find the contigous and sum up min and max
"""

import fileinput
import numpy as np


def get_list_nums(input_txt):
    list_of_nums = []
    for line in fileinput.input(input_txt):
        num = int(line.rstrip())
        list_of_nums.append(num)

    return list_of_nums


def check_valid(small_list, total_sum):
    for num in small_list:
        diff = total_sum - num
        if diff in small_list:
            status = True
            break
        else:
            status = False

    return status


def min_sum(list_of_nums, step):
    check_list_nums = list_of_nums[step:]

    for i, num in enumerate(check_list_nums):
        small_list = list_of_nums[i:i + step]
        status = check_valid(small_list, num)
        if status == False:
            return num


def find_contiguous_nums(list_of_num, total_sum):
    len_list = len(list_of_num)
    for step in range(2, len_list):
        multi_list = [None] * step
        for i in range(step):
            multi_list[i] = list_of_num[i:]

        min_len = len(multi_list[-1])
        for i, l in enumerate(multi_list):
            multi_list[i] = l[0:min_len]

        numpy_array = np.asarray(multi_list)
        sum_array = np.sum(numpy_array, 0)
        idx = np.where(sum_array == total_sum)
        if len(idx[0]):
            ans_np = numpy_array[:, idx[0][0]]
            return ans_np.min() + ans_np.max()


if __name__ == "__main__":

    list_of_nums = get_list_nums('./input.txt')
    step = 25
    # list_of_nums = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117,
                    # 150, 182, 127, 219, 299, 277, 309, 576]
    # step = 5

    ans = min_sum(list_of_nums, step)
    idx = list_of_nums.index(ans)

    new_list_of_nums = list_of_nums[:idx]
    ans = find_contiguous_nums(new_list_of_nums, ans)
    print(f'Answer: {ans}')
