"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: docs
"""

import fileinput


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


if __name__ == "__main__":

    list_of_nums = get_list_nums('./input.txt')
    step = 25
    ans = min_sum(list_of_nums, step)
    print(f'Answer: {ans}')
