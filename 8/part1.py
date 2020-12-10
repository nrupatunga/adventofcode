"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: finding the accumulator value
"""
import fileinput


def find_acc_val(data, visited, accumulator=0):
    idx = 0
    while True:
        if visited[idx]:
            break

        inst, val = data[idx].split()
        val = int(val)
        visited[idx] = 1
        if inst == 'acc':
            accumulator += val
            idx = idx + 1
        elif inst == 'jmp':
            idx = idx + val
        elif inst == 'nop':
            idx = idx + 1

    return accumulator


if __name__ == "__main__":
    ans = 0
    data = []
    for i, line in enumerate(fileinput.input('./input.txt')):
        data.append(line.rstrip())

    visited = [0] * len(data)
    ans = find_acc_val(data, visited)
    print(f'Answer: {ans}')
