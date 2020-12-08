"""
File: seat_id.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: finding the seat id
"""
import fileinput

from rich import print


def decode_row(seat_row, dbg=False):
    assert len(seat_row) == 7

    start, end = 0, 127
    for i, char in enumerate(seat_row):
        if char == 'F':
            step = (end - start) + 1
            step = int(step * 0.5) - 1
            end = start + step
        elif char == 'B':
            step = (end - start) + 1
            step = int(step * 0.5)
            start = start + step

        if dbg:
            print(f'({i}). start: {start}, end: {end}')

    assert min(start, end) == start

    return min(start, end)


def decode_col(seat_col, dbg=False):
    assert len(seat_col) == 3

    start, end = 0, 7
    for i, char in enumerate(seat_col):
        if char == 'L':
            step = (end - start) + 1
            step = int(step * 0.5) - 1
            end = start + step
        elif char == 'R':
            step = (end - start) + 1
            step = int(step * 0.5)
            start = start + step

        if dbg:
            print(f'({i}). start: {start}, end: {end}')

    assert max(start, end) == end

    return max(start, end)


Answers = []
for line in fileinput.input('./input.txt'):
    seat = line.rstrip()
    seat_7 = seat[0:7]
    seat_3 = seat[7:]
    row = decode_row(seat_7)
    col = decode_col(seat_3)
    seat_id = row * 8 + col
    Answers.append(seat_id)

print(f'Answer: {max(Answers)}')
