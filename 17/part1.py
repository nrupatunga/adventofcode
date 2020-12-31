"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: 6 cycles cube lighting
"""

import fileinput
from collections import Counter


def neighbors_coords(left, right):
    neighbors = []
    for i in range(left, right):
        for j in range(left, right):
            for k in range(left, right):
                if i == 0 and j == 0 and k == 0:
                    continue
                neighbors.append([i, j, k])

    return neighbors


def find_xyz_range(z):
    z_range = len(z)
    y_range = len(z[0])
    x_range = len(z[0][0])

    return x_range, y_range, z_range


def read_input(input_txt):
    z = [[], [], []]
    z_1 = []
    for line in fileinput.input(input_txt):
        line = line.rstrip()
        row = []
        for char in line:
            if char == '.':
                row.append(0)
            else:
                row.append(1)
        z_1.append(row)

    row_len = len(z_1[0])
    z_0 = [[0, 0, 0]] * row_len
    z_2 = [[0, 0, 0]] * row_len

    z[0] = z_0
    z[1] = z_1
    z[2] = z_2

    return z


def get_new_state(z, curr_coord, limits, coords):
    i, j, k = curr_coord
    curr_state = z[i][j][k]
    x_r, y_r, z_r = limits
    x_r, y_r, z_r = x_r - 1, y_r - 1, z_r - 1
    vals = []
    for n_1, n_2, n_3 in coords:
        i_new, j_new, k_new = i + n_1, j + n_2, k + n_3

        if i_new == i and j_new == j and k_new == k:
            continue

        if i_new < 0 or j_new < 0 or k_new < 0:
            continue
        if i_new > z_r or j_new > y_r or k_new > x_r:
            continue

        vals.append(z[i_new][j_new][k_new])

    __import__('pdb').set_trace()
    counts = Counter(vals)

    if curr_state == 1 and (counts[1] == 2 or counts[1] == 3):
        new_state = 1
    else:
        new_state = 0

    if curr_state == 0 and counts[1] == 3:
        new_state = 1
    else:
        new_state = 0

    return new_state


def get_new_z(z, x_r, y_r, z_r, neighbors):
    __import__('pdb').set_trace()
    for i in range(z_r):
        for j in range(y_r):
            for k in range(x_r):
                new_state = get_new_state(
                    z, (i, j, k), (x_r, y_r, z_r), neighbors)
                z[i][j][k] = new_state

    return z


def main(input_txt, dbg=True):
    z = read_input(input_txt)
    neighbors = neighbors_coords(-1, 2)
    x_r, y_r, z_r = find_xyz_range(z)
    for i in range(1):
        z_new = get_new_z(z, x_r, y_r, z_r, neighbors)

    if dbg:
        import numpy as np
        print(np.asarray(z))
        print(np.asarray(z_new))


if __name__ == "__main__":
    ans = main('./dummy.txt')
    print(f'Answer: {ans}')
