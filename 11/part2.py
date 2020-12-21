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


def get_input_in_array(input_txt):
    list_of_nums = []
    for line in fileinput.input(input_txt):
        line = (line.rstrip())
        line = line.replace('L', '0')
        line = line.replace('.', '1')
        chars = [char for char in line]
        nums = list(map(int, chars))
        list_of_nums.append(nums)

    data = np.asarray(list_of_nums)
    data[data == 1] = -1
    return data


def find_indices(rows, cols):
    min_len = min(rows.size, cols.size)
    rows = rows[0: min_len]
    cols = cols[0: min_len]
    indices = rows * 98 + cols
    return indices


def check_diag_tl(data, i, j):
    h, w = data.shape

    try:
        rows = np.arange(i - 1, -1, -1)
        cols = np.arange(j - 1, -1, -1)
        indices = find_indices(rows, cols)
    except ValueError:
        return None

    if indices.size == 0:
        return None

    data_ = data.ravel()[indices]
    idx = np.argmax(data_ > -1)
    return data_[idx]


def check_diag_tr(data, i, j):
    h, w = data.shape

    try:
        rows = np.arange(i - 1, -1, -1)
        cols = np.arange(j + 1, w)
        indices = find_indices(rows, cols)
    except ValueError:
        return None

    if indices.size == 0:
        return None

    data_ = data.ravel()[indices]
    idx = np.argmax(data_ > -1)
    return data_[idx]


def check_diag_br(data, i, j):
    h, w = data.shape

    try:
        rows = np.arange(i + 1, h)
        cols = np.arange(j + 1, w)
        indices = find_indices(rows, cols)
    except ValueError:
        return None

    if indices.size == 0:
        return None

    data_ = data.ravel()[indices]
    idx = np.argmax(data_ > -1)
    return data_[idx]


def check_diag_bl(data, i, j):
    h, w = data.shape

    try:
        rows = np.arange(i + 1, h)
        cols = np.arange(j - 1, -1, -1)
        indices = find_indices(rows, cols)
    except ValueError:
        return None

    if indices.size == 0:
        return None

    data_ = data.ravel()[indices]
    idx = np.argmax(data_ > -1)
    return data_[idx]


def check_bottom(data, i, j):
    h, w = data.shape

    try:
        indices = np.arange(i + 1, h) * 10 + j
    except ValueError:
        return None

    if indices.size == 0:
        return None

    data_ = data.ravel()[indices]
    idx = np.argmax(data_ > -1)
    return data_[idx]


def check_top(data, i, j):
    h, w = data.shape
    try:
        indices = np.arange(i - 1, -1, -1) * 10 + j
    except ValueError:
        return None

    if indices.size == 0:
        return None

    data_ = data.ravel()[indices]
    idx = np.argmax(data_ > -1)
    return data_[idx]


def check_left(data, i, j):
    h, w = data.shape
    try:
        indices = i * np.array(h) + np.arange(j - 1, -1, -1)
    except ValueError:
        return None

    if indices.size == 0:
        return None

    data_ = data.ravel()[indices]
    idx = np.argmax(data_ > -1)
    return data_[idx]


def check_right(data, i, j):
    h, w = data.shape
    indices = i * np.array(h) + np.arange(j + 1, w)
    if indices.size == 0:
        return None

    data_ = data.ravel()[indices]
    idx = np.argmax(data_ > -1)
    return data_[idx]


def add_to_neighbors(neighbors, element):
    if element is not None:
        neighbors.append(element)

    return neighbors


def get_seat_arrangements(data):
    new_data = np.zeros_like(data)
    num_rows = data.shape[0]
    num_cols = data.shape[1]

    # occupied = 1, empty = 0
    status = -1
    neighbors = []
    for i in range(num_rows):
        for j in range(num_cols):
            neighbors = add_to_neighbors(neighbors, check_right(data, i, j))
            neighbors = add_to_neighbors(neighbors, check_left(data, i, j))
            neighbors = add_to_neighbors(neighbors, check_top(data, i, j))
            neighbors = add_to_neighbors(neighbors, check_bottom(data, i, j))
            neighbors = add_to_neighbors(neighbors, check_diag_tl(data, i, j))
            neighbors = add_to_neighbors(neighbors, check_diag_br(data, i, j))
            neighbors = add_to_neighbors(neighbors, check_diag_bl(data, i, j))
            neighbors = add_to_neighbors(neighbors, check_diag_tr(data, i, j))

            num_seats_occupied = neighbors.count(1)
            if data[i, j] == 0 and (1 not in neighbors):
                new_data[i, j] = 1
            elif data[i, j] == 1 and num_seats_occupied >= 5:
                new_data[i, j] = 0
            else:
                new_data[i, j] = data[i, j]

            neighbors = []

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
