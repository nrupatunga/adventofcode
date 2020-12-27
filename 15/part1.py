"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: memory game
"""
import fileinput


list_of_nums = []


def main(input_txt):
    for line in fileinput.input(input_txt):
        nums = list(map(int, line.rstrip().split(',')))
        while True:
            if len(nums) == 2020:
                break

            last_num = nums[-1]
            last_index = len(nums)

            if last_num in nums[:last_index - 1]:
                idxs = [idx for idx, val in enumerate(
                    nums[:-1]) if last_num == val]
                prev_index = idxs[-1] + 1
                curr_num = last_index - prev_index
            else:
                curr_num = 0

            nums.append(curr_num)

    return nums[-1]


if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')
