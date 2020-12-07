"""
File: 2_valid_passports.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: find valid passports
"""
import fileinput

from rich import print

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def validate(data):
    """validate passport data"""

    key = 'byr'
    val = int(data[key])
    if val < 1920 or val > 2002:
        return False

    key = 'iyr'
    val = int(data[key])
    if val < 2010 or val > 2020:
        return False

    key = 'eyr'
    val = int(data[key])
    if val < 2020 or val > 2030:
        return False

    key = 'hgt'
    val = data[key]
    if 'cm' in val:
        val = int(val.split('cm')[0])
        if val < 150 or val > 193:
            return False
    elif 'in' in val:
        val = int(val.split('in')[0])
        if val < 59 or val > 76:
            return False
    else:
        return False

    key = 'hcl'
    val = data[key]
    if val[0] != '#':
        return False

    val = val[1:]
    valid_letters = ['a', 'b', 'c', 'd', 'e', 'f']
    if not all(c.isdigit() or (c.islower() and c in valid_letters) for c in val):
        return False

    key = 'ecl'
    val = data[key]
    ecl_vals = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if val not in ecl_vals:
        return False

    key = 'pid'
    val = data[key]
    if len(val) != 9:
        return False

    val = int(val)
    if val < 0 and val > 999999999:
        return False

    return True


def process(data, required_fields):
    new_data = ' '.join(string for string in data)
    new_data = new_data.rstrip().split()
    keys = []

    passport_dict = {}
    for info in new_data:
        key, value = info.split(':')
        if key != 'cid':
            assert (key in required_fields), f'{key} not present'
            passport_dict[key] = value

    keys = list(passport_dict.keys())
    for field in required_fields:
        if field not in keys:
            return False

    status = validate(passport_dict)
    return status


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
