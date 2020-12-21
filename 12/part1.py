"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: figure out the manhattan distance
"""
import fileinput

init_dir = 'E'

# distance covered in each directions
dist = {'E': 0, 'W': 0, 'N': 0, 'S': 0}

angle_dir_r = 'ESWN'
angle_dir_l = 'ENWS'


def get_change_dir(curr_dir, inst, angle):
    if inst == 'L':
        step = int((angle % 360) / 90)
        pos = [i for i, char in enumerate(angle_dir_l) if char == curr_dir][0]
        curr_dir = angle_dir_l[(pos + step) % len(angle_dir_l)]
    elif inst == 'R':
        step = int((angle % 360) / 90)
        pos = [i for i, char in enumerate(angle_dir_r) if char == curr_dir][0]
        curr_dir = angle_dir_r[(pos + step) % len(angle_dir_r)]

    return curr_dir


def main(input_txt):
    curr_dir = init_dir
    for line in fileinput.input(input_txt):
        line = line.rstrip()
        chars = list(line)

        curr_inst = chars[0]
        ang_or_dist = int(''.join(chars[1:]))

        if curr_inst == 'L' or curr_inst == 'R':
            curr_dir = get_change_dir(curr_dir, curr_inst, ang_or_dist)
        else:
            if curr_inst == 'F':
                curr_inst = curr_dir
            dist[curr_inst] = dist[curr_inst] + ang_or_dist


    manhattan_dist = abs(dist['E'] - dist['W']) + abs(dist['N'] - dist['S'])
    return manhattan_dist


if __name__ == "__main__":
    ans = main('./dummy.txt')
    print(f'Answer: {ans}')
