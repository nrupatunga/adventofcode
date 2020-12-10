"""
File: part2.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: how many bags should shiny gold bag contain
"""

import fileinput
import re
from collections import defaultdict
from time import time


def count_individual_bags(s):
    s = s.strip()

    try:
        num_bags = int(s[0])
    except ValueError:
        num_bags = 0

    result = ''.join([i for i in s if not i.isdigit()])
    result = result.strip()
    result = re.sub(r'[^\w\s]', '', result).rstrip()
    return {result: num_bags}


def get_bag_dict(data):
    bag_dict = {}
    for line in data:
        bags = line.rstrip().split('contain')
        bags = [bag.replace('bags', '').strip() for bag in bags]
        bags = [bag.replace('bag', '').strip() for bag in bags]
        parent = bags[0]
        children = bags[1].split(',')
        children = [count_individual_bags(child) for child in children]
        bag_dict[parent] = children
    return bag_dict


def get_curr_list(bag_dict, s):
    curr_list = bag_dict[s]
    res = defaultdict(list)
    {res[key].append(sub[key]) for sub in curr_list for key in sub}

    return res


ans = 0
# recursion
def count_all_bags(bag_dict, bags, scale=1):
    global ans
    for bag in bags:
        res = get_curr_list(bag_dict, bag)
        for key, item in res.items():
            if not item[0]:
                return
            ans += item[0] * scale
            new_scale = item[0] * scale
            count_all_bags(bag_dict, [key], new_scale)

    return ans


if __name__ == "__main__":
    start = time()
    ans = 0
    data = []
    for i, line in enumerate(fileinput.input('./input.txt')):
        data.append(line.rstrip())

    bag_dict = get_bag_dict(data)
    ans = count_all_bags(bag_dict, ['shiny gold'])
    print(f'Answer: {ans}')
    print(f'Total Time (ms): {(time() - start) * 1000}')
