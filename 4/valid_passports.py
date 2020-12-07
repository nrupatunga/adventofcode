"""
File: valid_passports.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: find valid passports
"""
import fileinput
from rich import print


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def process(data, required_fields):
    new_data = ' '.join(string for string in data)
    new_data = new_data.rstrip().split()
    keys = []

    for info in new_data:
        key = info.split(':')[0].lower()
        if key != 'cid':
            assert (key in required_fields), f'{key} not present'
            keys.append(key)

    for field in required_fields:
        if field not in keys:
            return False

    return True


passport_data = []
num_valid = 0
for i, line in enumerate(fileinput.input('./input.txt')):
    passport_data.append(line.rstrip())

    if line == '\n':
        status = process(passport_data, required_fields)
        passport_data = []
        if status:
            num_valid += 1

# last passport data is missed if not below logic
if len(passport_data):
    status = process(passport_data, required_fields)
    if status:
        num_valid += 1


print(f'Answer: {num_valid}')

