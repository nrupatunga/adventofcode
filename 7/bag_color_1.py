"""
File: bag_color_1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: find number of bags containing shiny gold bag
"""

import fileinput
import re

from rich import print


def remove_digit(s):
    result = ''.join([i for i in s if not i.isdigit()])
    result = result.strip()
    result = re.sub(r'[^\w\s]', '', result)
    return result


def get_bag_dict(data):
    bag_dict = {}
    for line in data:
        bags = line.rstrip().split('contain')
        bags = [bag.replace('bags', '').strip() for bag in bags]
        bags = [bag.replace('bag', '').strip() for bag in bags]
        parent = bags[0]
        children = bags[1].split(',')
        children = [remove_digit(child).rstrip() for child in children]
        bag_dict[parent] = children

    return bag_dict


def find_num_bags(data, bags):
    all_bags = []
    total = 0
    bag_dict = get_bag_dict(data)
    while len(bags):
        curr_bags = []
        for s in bags:
            for key, item in bag_dict.items():
                if s in item:
                    curr_bags.append(key)
                    all_bags.append(key)
                else:
                    continue

        bags = list(set(curr_bags))
        all_bags.extend(bags)

    total = len(set(all_bags))
    return total, all_bags


if __name__ == "__main__":
    ans = 0
    data = []
    for i, line in enumerate(fileinput.input('./input.txt')):
        data.append(line.rstrip())

    ans, bags = find_num_bags(data, ['shiny gold'])

    print(f'Answer: {ans}')
