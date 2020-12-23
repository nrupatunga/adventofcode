"""
File: part2.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: move ship wrt waypoint
"""
import fileinput

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


def ship_to_waypoint(waypoint, scale=10):
    for wp_dir in waypoint:
        chars = list(wp_dir)
        curr_inst = chars[-1]
        ang_or_dist = int(''.join(chars[:-1]))
        dist[curr_inst] = dist[curr_inst] + scale * ang_or_dist


def move_waypoint(waypoint, inst, dist):
    for i, wp_dir in enumerate(waypoint):
        chars = list(wp_dir)
        curr_inst = chars[-1]
        if curr_inst == inst:
            ang_or_dist = int(''.join(chars[:-1]))
            ang_or_dist = ang_or_dist + dist
            waypoint[i] = ''.join([str(ang_or_dist), curr_inst])
        elif curr_inst in 'WE' and inst in 'WE':
            ang_or_dist = int(''.join(chars[:-1]))
            ang_or_dist = ang_or_dist - dist
            waypoint[i] = ''.join([str(ang_or_dist), curr_inst])
        elif curr_inst in 'NS' and inst in 'NS':
            ang_or_dist = int(''.join(chars[:-1]))
            ang_or_dist = ang_or_dist - dist
            waypoint[i] = ''.join([str(ang_or_dist), curr_inst])

    return waypoint


def change_waypoint_direction(waypoint, inst, angle):
    for i, wp_dir in enumerate(waypoint):
        chars = list(wp_dir)
        curr_dir = chars[-1]
        new_dir = get_change_dir(curr_dir, inst, angle)
        waypoint[i] = waypoint[i].replace(curr_dir, new_dir)

    return waypoint


def main(input_txt):
    waypoint = ['10E', '1N']
    for line in fileinput.input(input_txt):
        line = line.rstrip()
        chars = list(line)

        curr_inst = chars[0]
        ang_or_dist = int(''.join(chars[1:]))

        if curr_inst == 'F':
            ship_to_waypoint(waypoint, scale=ang_or_dist)
        elif curr_inst == 'L' or curr_inst == 'R':
            waypoint = change_waypoint_direction(waypoint, curr_inst,
                                                 ang_or_dist)
        else:
            waypoint = move_waypoint(waypoint, curr_inst, ang_or_dist)

    manhattan_dist = abs(dist['E'] - dist['W']) + abs(dist['N'] - dist['S'])
    return manhattan_dist

if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')
