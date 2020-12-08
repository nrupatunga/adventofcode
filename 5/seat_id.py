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


def find_my_seat(seat_ids):
    seat_ids = sorted(seat_ids)
    all_seat_ids = set(list(range(seat_ids[0], seat_ids[-1] + 1)))
    seat_ids = set(seat_ids)
    my_seat_id = all_seat_ids - seat_ids
    my_seat_id = list(my_seat_id)[0]

    return my_seat_id


part_1_ans = []

for line in fileinput.input('./input.txt'):
    seat = line.rstrip()
    seat_7 = seat[0:7]
    seat_3 = seat[7:]
    row = decode_row(seat_7)
    col = decode_col(seat_3)
    seat_id = row * 8 + col
    part_1_ans.append(seat_id)

my_seat_id = find_my_seat(part_1_ans)
print(f'Answer-1: {max(part_1_ans)}')
print(f'Answer-2: {my_seat_id}')
