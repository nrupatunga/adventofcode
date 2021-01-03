"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: matching tile
"""

import fileinput
from functools import reduce


def get_borders(tile_data):
    b = []
    b.append(tile_data[0])
    b.append(tile_data[-1])
    border = [t[0] for t in tile_data]
    b.append(''.join(border))
    border = [t[-1] for t in tile_data]
    b.append(''.join(border))

    return b


def compare_tile(tile, tile_dict, tile_no, index):
    border = tile[index]
    border_list = []
    border_list_r = []

    for key, item in tile_dict.items():
        if key == tile_no:
            continue
        for b in item:
            border_list.append(b)
            border_list_r.append(b[::-1])

    status = False
    border_r = border[::-1]
    status = border in border_list or border in border_list_r
    status = status or (border_r in border_list or border_r in border_list_r)

    return status


def find_corner_tiles(tile_dict):
    corners = []
    for tile_no, tile in tile_dict.items():
        num_matches = 0
        for i in range(4):
            status = compare_tile(tile, tile_dict, tile_no, i)
            if status:
                num_matches += 1

        if num_matches == 2:
            corners.append(tile_no)

    return corners


def tile_borders(input_file):
    tile = False
    tile_dict = {}
    tile_data = []
    for line in fileinput.input(input_file):
        line = line.strip()
        if line == '':
            borders = get_borders(tile_data)
            tile = False
            tile_dict[tile_no] = borders

        if tile:
            tile_data.append(line)

        if 'Tile' in line:
            tile_no = int(line.split(':')[0].split(' ')[-1])
            tile = True
            tile_data = []

    return tile_dict


def main(input_file):
    tile_dict = tile_borders(input_file)
    corners = find_corner_tiles(tile_dict)
    ans = reduce((lambda x, y: x * y), corners)
    return ans


if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')

