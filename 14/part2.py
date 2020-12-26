"""
File: part2.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: sum of all the values in the memory
"""

import fileinput


def find_mem_locs(value, mask):
    num_floats = 0
    float_locs = []
    possible_locs = []
    for i, letter in enumerate(mask):
        if letter == '0':
            continue

        if letter == 'X':
            num_floats += 1
            float_locs.append(i)

        value = value[:i] + letter + value[i + 1:]

    num_combinations = pow(2, num_floats)
    for i in range(num_combinations):
        bin_value = format(i, f'0{num_floats}b')
        for j, val in enumerate(bin_value):
            loc = float_locs[j]
            value = value[:loc] + val + value[loc + 1:]

        possible_locs.append(int(value, 2))

    return possible_locs


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
            mem_loc = int(a.split('[')[1].split(']')[0])
            bin_value = format(mem_loc, '036b')
            run = True

        if run:
            mem_locs = find_mem_locs(bin_value, mask_str)
            for i in mem_locs:
                mem_map[i] = value

    for key, value in mem_map.items():
        ans = ans + value

    return ans


if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')
