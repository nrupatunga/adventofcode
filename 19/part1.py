"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: I found this problem hard, and I tried to solve with
different logic but ended up with crappy solution, so had to look up
online to understand the logic to solve, this is not my solution. But
coded after understanding it
"""

import fileinput


rules_dict = {}
strings_list = []


def get_rules(input_file):
    status = True
    for line in fileinput.input(input_file):
        line = line.strip()
        if line == '':
            status = False
            continue

        if status:
            rule_no, rules = line.split(':')
            rules = rules.strip()
            rules_dict[int(rule_no)] = rules
        else:
            strings_list.append(line)

    return rules_dict, strings_list


def check_valid(line, rule_no):
    rules = rules_dict[rule_no]
    if rules.strip('"').isalpha():
        char = rules.strip('"')
        if line[0] == char:
            return 1
        else:
            return -1

    __import__('pdb').set_trace()
    for rule in rules.split('|'):
        match_len = 0
        for r_n in rule.strip().split(' '):
            ret = check_valid(line[match_len:], int(r_n))
            if ret == -1:
                match_len = -1
                break
            match_len += ret

        if match_len != -1:
            return match_len

    return -1


def main(input_file):
    ans = 0
    get_rules(input_file)
    for line in strings_list:
        length = check_valid(line, 0)
        if length == len(line):
            ans = ans + 1

    return ans


if __name__ == "__main__":
    ans = main('./dummy.txt')
    print(f'Answer: {ans}')
