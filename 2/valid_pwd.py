"""
File: valid_pwd.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: find valid passwords
"""

import fileinput


def process(line):
    line = line.strip().split()
    low, high = line[0].split('-')
    low, high = int(low), int(high)

    character = line[1].split(':')[0]
    password = line[-1]

    return (low, high), character, password


def is_valid_password_new(data):
    (low, high), character, password = process(data)
    low = low - 1
    high = high - 1
    if password[low] == character and password[high] != character:
        print(process(data))
        return True
    elif password[low] != character and password[high] == character:
        print(process(data))
        return True
    else:
        return False

def is_valid_password(data):
    (low, high), character, password = process(data)
    count = password.count(character)
    if count >= low and count <= high:
        print(process(data))
        return True
    else:
        return False


total = 0
for line in fileinput.input('./input.txt'):
    # status = is_valid_password(line)
    status = is_valid_password_new(line)
    if status:
        total = total + 1

print(f'Number of valid passwords: {total}')
