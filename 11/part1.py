"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: total number of seats at the end occupied
"""

import fileinput
import itertools
import operator

import numpy as np

x = [-1, 0, 1]
y = [-1, 0, 1]
idx = list(itertools.product(x, y))
idx.remove((0, 0))


def get_input_in_array(input_txt):
    list_of_nums = []
    for line in fileinput.input(input_txt):
        line = (line.rstrip())
        line = line.replace('L', '0')
        line = line.replace('.', '2')
        chars = [char for char in line]
        nums = list(map(int, chars))
        list_of_nums.append(nums)

    return np.asarray(list_of_nums)


def neighbor_seat_status(data, i, j):
    curr_idx = [i, j]
    neighbors = np.asarray(curr_idx) + np.asarray(idx)
    neighbors[:, 0] = np.clip(neighbors[:, 0], 0, data.shape[0] - 1)
    neighbors[:, 1] = np.clip(neighbors[:, 1], 0, data.shape[1] - 1)

    neighbors = neighbors.tolist()
    neighbors_new = neighbors.copy()
    for item in neighbors:
        if item == [i, j]:
            neighbors_new.remove(item)

    neighbors = [list(x) for x in set(tuple(x) for x in neighbors_new)]
    seat_status = []
    for pos in neighbors:
        seat_status.append(data[pos[0], pos[1]])

    status = -1
    if 1 not in seat_status:
        status = 0
    else:
        num_seats_occupied = seat_status.count(1)
        if data[i, j] == 1 and num_seats_occupied >= 4:
            status = 1
        elif data[i, j] == 0 and num_seats_occupied > 0:
            status = 1
        else:
            status = 0

    return status


def get_seat_arrangements(data):
    new_data = np.zeros_like(data)
    num_rows = data.shape[0]
    num_cols = data.shape[1]

    # occupied = 1, empty = 0
    status = -1
    for i in range(num_rows):
        for j in range(num_cols):
            status = neighbor_seat_status(data, i, j)
            if data[i, j] == 0 and status == 0:
                new_data[i, j] = 1
            elif data[i, j] == 1 and status == 1:
                new_data[i, j] = 0
            else:
                new_data[i, j] = data[i, j]

    return new_data


if __name__ == "__main__":
    data = get_input_in_array('./input.txt')
    while True:
        new_data = get_seat_arrangements(data.copy())
        if (new_data == data).all():
            break
        data = new_data

    ans = (new_data == 1).sum()
    print(f'Answer = {ans}')
