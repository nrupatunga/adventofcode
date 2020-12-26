"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: sum of all the values in the memory
"""

import fileinput


def modify_bit(value, mask):
    for i, letter in enumerate(mask):
        if letter == 'X':
            continue

        value = value[:i] + letter + value[i + 1:]

    return int(value, 2)


def main(input_txt):
    mem_map = {}
    ans = 0
    for line in fileinput.input(input_txt):
        a, b = line.split('=')
        if a.rstrip() == 'mask':
            mask_str = b.strip()
            run = False
        else:
            value = int(b.strip())
            bin_value = format(value, '036b')
            mem_loc = a.split('[')[1].split(']')[0]
            run = True

        if run:
            new_value = modify_bit(bin_value, mask_str)
            mem_map[mem_loc] = new_value

    for key, value in mem_map.items():
        ans = ans + value

    return ans


if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')
