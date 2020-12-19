"""
File: part2.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: finding all possible ways of connecting the adapters
"""
import fileinput
import numpy as np

ans = 0

def get_list_nums(input_txt):
    list_of_nums = []
    for line in fileinput.input(input_txt):
        num = int(line.rstrip())
        list_of_nums.append(num)

    return list_of_nums


def is_equal_to_max_jolts(curr_list, max_jolts):
    for item in curr_list:
        if item != max_jolts:
            return False

    return True


def num_possible_paths(seeds, list_of_nums, max_jolts):
    global ans
    curr_possible_paths = []
    for item in seeds:
        if item == max_jolts:
            curr_possible_paths.append(item)
        else:
            for i in range(1, 4):
                if (i + item) in list_of_nums:
                    curr_possible_paths.append(i + item)

    found = is_equal_to_max_jolts(curr_possible_paths, max_jolts)
    if found:
        ans = len(curr_possible_paths)
        return
    else:
        num_possible_paths(curr_possible_paths,
                           list_of_nums, max_jolts)



if __name__ == "__main__":
    list_of_nums = get_list_nums('./input.txt')
    list_of_nums = sorted(list_of_nums)
    max_jolts = max(list_of_nums)
    num_possible_paths([0], list_of_nums, max_jolts)
    print(f'Answer: {ans}')

