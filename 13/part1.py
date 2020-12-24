"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: which bus to take
"""

import fileinput

import numpy as np


def get_input(input_txt):
    for i, line in enumerate(fileinput.input(input_txt)):
        if i == 0:
            timestamp = int(line.rstrip())
        else:
            bus_ids = line.rstrip().split(',')
            bus_ids = [int(x) for x in bus_ids if x is not 'x']

    return timestamp, bus_ids


def main(input_txt):
    timestamp, bus_ids = get_input(input_txt)
    init_timestamp = timestamp
    while True:
        output = np.asarray(timestamp) / np.asarray(bus_ids)
        diff = output - output.astype(np.int)
        idx = np.where(diff == 0.)[0]
        if idx.size > 0:
            break
        timestamp = timestamp + 1

    return (timestamp - init_timestamp) * bus_ids[idx[0]]


if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')
