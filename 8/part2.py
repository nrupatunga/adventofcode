"""
File: part2.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: finding corrupt instruction
"""
import fileinput


def find_acc_val(data, visited, accumulator=0):
    idx = 0

    status = True
    while True:
        if idx == len(visited):
            status = True
            break

        if visited[idx]:
            status = False
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

    return status, accumulator


if __name__ == "__main__":
    ans = 0
    data = []
    jmp_loc = []
    for i, line in enumerate(fileinput.input('./input.txt')):
        data.append(line.rstrip())
        inst, _= line.rstrip().split()
        if inst == 'jmp':
            jmp_loc.append(i)

    for i in jmp_loc:
        visited = [0] * len(data)
        data_new = data.copy()
        data_new[i] = data_new[i].replace('jmp', 'nop')
        status, ans = find_acc_val(data_new, visited)
        if status:
            print(f'Answer: {ans}')
            break
