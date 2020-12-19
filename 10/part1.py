"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description:
"""
import fileinput
import numpy as np


def get_list_nums(input_txt):
    list_of_nums = []
    for line in fileinput.input(input_txt):
        num = int(line.rstrip())
        list_of_nums.append(num)

    return list_of_nums


if __name__ == "__main__":

    list_of_nums = get_list_nums('./input.txt')
    # list_of_nums = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    # list_of_nums = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49,
                    # 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4,
                    # 2, 34, 10, 3]
    list_of_nums = sorted(list_of_nums)
    diff_jolts = np.diff(list_of_nums)
    ans = (sum(diff_jolts == 3) + 1) * (sum(diff_jolts == 1) + 1)
    print(f'Answer: {ans}')
