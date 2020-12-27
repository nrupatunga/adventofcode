"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: find error rate
"""

import fileinput


def main(input_txt):
    valid_numbers = []
    invalid_tickets = []
    read_rules = True
    read_tickets = False
    for line in fileinput.input(input_txt):
        if line == '\n':
            read_rules = False
            continue

        if read_rules:
            a, b = line.strip().split(':')[-1].split('or')
            a, b = a.strip(), b.strip()
            range1 = a.split('-')
            range2 = b.split('-')

            range_1 = list(map(int, range1))
            range_2 = list(map(int, range2))

            valid_numbers.extend(list(range(range_1[0], range_1[1] + 1)))
            valid_numbers.extend(list(range(range_2[0], range_2[1] + 1)))
        elif read_tickets:
            ticket_numbers = line.strip().split(',')
            ticket_numbers = list(map(int, ticket_numbers))
            invalid_tickets.extend(list(set(ticket_numbers) -
                                        set(valid_numbers)))

        if line.strip() == 'nearby tickets:':
            read_tickets = True
            valid_numbers = list(set(valid_numbers))

    ans = 0
    for item in invalid_tickets:
        ans = ans + item

    return ans


if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')
