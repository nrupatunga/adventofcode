"""
File: count_trees.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: count trees
"""

import fileinput


input_m_c = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def count_trees(m=3, ci=1):
    skip_interval = ci - 1
    pos = 0
    num_trees = 0
    for i, line in enumerate(fileinput.input('./input.txt')):
        line = line.strip()
        if i == 0:
            continue

        if skip_interval > 0:
            skip_interval = skip_interval - 1
            continue

        skip_interval = ci - 1
        pos = pos + m
        width = len(line)
        pos = pos % width
        assert (pos != -1)

        if line[pos] == '#':
            num_trees += 1

    return num_trees

final_prod = 1
for m, c in input_m_c:
    final_prod = final_prod * count_trees(m, c)

print(f'Answer: {final_prod}')
