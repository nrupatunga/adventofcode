"""
File: part2.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: counting the number of active cubes
"""

import fileinput
from itertools import product


active_cubes = set()


def get_active_cubes(input_file):
    z = 0
    for y, line in enumerate(fileinput.input(input_file)):
        line = line.rstrip()
        for x, char in enumerate(line):
            if char == '#':
                active_cubes.add((0, 0, y, x))

    dim = len(line)
    return active_cubes, dim


def find_neighbors(cube, cube_dim):
    for coord in product((-1, 0, 1), repeat=cube_dim):
        if coord != (0, 0, 0, 0):
            new_coord = (cube[0] + coord[0], cube[1] + coord[1], cube[2]
                         + coord[2], cube[3] + coord[3])
            yield new_coord

def update_active_cubes(active_cubes, ngbr, new_active_cubes, cube_dim):
    curr_state = 0
    if ngbr in active_cubes:
        curr_state = 1

    num_actives = 0
    for neighbor in find_neighbors(ngbr, cube_dim):
        if neighbor in active_cubes:
            num_actives += 1

    if curr_state == 1 and  num_actives in [2, 3]:
        new_active_cubes.add(ngbr)

    if curr_state == 0 and  num_actives == 3:
        new_active_cubes.add(ngbr)

    return new_active_cubes


def main(input_file, cube_dim=3):
    active_cubes, dim = get_active_cubes(input_file)
    for _ in range(6):
        new_active_cubes = set()
        for cube in active_cubes:
            new_active_cubes = update_active_cubes(active_cubes, cube,
                                                   new_active_cubes, cube_dim)
            for ngbr in find_neighbors(cube, cube_dim):
                new_active_cubes = update_active_cubes(active_cubes,
                                                       ngbr,
                                                       new_active_cubes,
                                                       cube_dim)
        active_cubes = new_active_cubes

    return len(new_active_cubes)


if __name__ == "__main__":
    ans = main('./input.txt', 4)
    print(f'Answer: {ans}')
