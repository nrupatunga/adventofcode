"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: memory game
"""
import fileinput


def main(input_txt, nth=2020):
    for line in fileinput.input(input_txt):
        nums = list(map(int, line.rstrip().split(',')))

    last_seen = [0] * nth
    for i, item in enumerate(nums[:-1]):
        last_seen[item] = i + 1

    curr_num = nums[-1]
    start_idx = len(nums)
    last_idx = len(nums) - 1
    for i in range(start_idx, nth):

        # first time
        if last_seen[curr_num] == 0:
            last_seen[curr_num] = i
            curr_num = 0
        else:
            new_num = i - last_seen[curr_num]
            last_seen[curr_num] = i
            curr_num = new_num

    return curr_num



if __name__ == "__main__":
    ans = main('./input.txt', nth=30000000)
    print(f'Answer: {ans}')
