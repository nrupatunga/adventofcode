"""
File: part2.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: finding the consecutive time stamps for bus ids
"""

import fileinput

import numpy as np


def get_input(input_txt):
    for i, line in enumerate(fileinput.input(input_txt)):
        if i == 0:
            timestamp = int(line.rstrip())
        else:
            bus_ids = line.rstrip().split(',')
            interval = [i for i, x in enumerate(bus_ids) if x is not 'x']
            bus_ids = [int(x) for x in bus_ids if x is not 'x']

    return timestamp, bus_ids, interval


def main(input_txt):
    _, bus_ids, interval = get_input(input_txt)

    bus_ids = np.asarray(bus_ids)
    interval = np.asarray(interval)

    x = 100000000000000
    step = 1e6
    y = x + step

    ids = [[]] * len(bus_ids)
    num_step = 0
    while True:
        print(f'Iteration: {y}')
        num = np.arange(x, y)
        for i, den in enumerate(bus_ids):
            output = num / den
            diff = output - output.astype(np.int)
            ids[i] = np.where(diff == 0) - interval[i]
            ids[i] = ids[i].tolist()[0]

        res = list(set.intersection(*map(set, ids))) 
        if res:
            break

        x = y
        y = x + step
        num_step = num_step + 1

    return int((res[0] + 1) + (num_step * step))


if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')
