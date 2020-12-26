"""
File: part2.opt.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: optimize implementation for part2
"""
import fileinput
from math import gcd


def get_input(input_txt):
    for i, line in enumerate(fileinput.input(input_txt)):
        if i == 0:
            timestamp = int(line.rstrip())
        else:
            bus_ids = line.rstrip().split(',')
            interval = [i for i, x in enumerate(bus_ids) if x is not 'x']
            bus_ids = [int(x) for x in bus_ids if x is not 'x']

    return timestamp, bus_ids, interval


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main(input_txt):
    _, bus_ids, interval = get_input(input_txt)
    b_0 = bus_ids[0]
    t = interval[0]
    for diff, b in zip(interval[1:], bus_ids[1:]):
        while True:
            if (t + diff) % b == 0:
                break
            t = t + b_0

        b_0 = lcm(b_0, b)

    return t


if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')
