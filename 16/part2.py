"""
File: part2.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: find error rate
"""

import fileinput


def main(input_txt):
    all_valid_tickets = []
    class_ranges = {}
    valid_row_tickets = []

    read_rules = True
    read_tickets = False
    read_your_ticket = False
    rows = 0
    cols = 0

    for line in fileinput.input(input_txt):
        if line == '\n':
            read_rules = False
            continue

        if read_your_ticket:
            ticket_numbers = line.strip().split(',')
            ticket_numbers = list(map(int, ticket_numbers))
            valid_row_tickets.extend(ticket_numbers)
            read_your_ticket = False

        if read_rules:
            valid_tickets = []
            key = line.strip().split(':')[0]
            a, b = line.strip().split(':')[-1].split('or')
            a, b = a.strip(), b.strip()
            range1 = a.split('-')
            range2 = b.split('-')

            range_1 = list(map(int, range1))
            range_2 = list(map(int, range2))

            valid_tickets.extend(list(range(range_1[0], range_1[1] + 1)))
            valid_tickets.extend(list(range(range_2[0], range_2[1] + 1)))
            all_valid_tickets.extend(valid_tickets)
            if 'departure' in key:
                class_ranges[key] = valid_tickets
            cols = cols + 1
        elif read_tickets:
            ticket_numbers = line.strip().split(',')
            ticket_numbers = list(map(int, ticket_numbers))
            status = len(set(ticket_numbers) - set(all_valid_tickets)) == 0
            if status:
                valid_row_tickets.extend(ticket_numbers)
                rows = rows + 1

        if line.strip() == 'nearby tickets:':
            read_tickets = True
            all_valid_tickets = list(set(all_valid_tickets))

        if line.strip() == 'your ticket:':
            read_your_ticket = True

    fields = []
    idxs_in_order = []
    while True:
        total_keys = len(class_ranges.keys())

        if len(idxs_in_order) == total_keys:
            break

        for i in range(cols):
            idxs = list(range(i, len(valid_row_tickets), cols))
            col_i = [valid_row_tickets[j] for j in idxs]
            local_fields = []
            if i in idxs_in_order:
                continue

            for key, item in class_ranges.items():
                if not len(set(col_i) - set(item)) and key not in fields:
                    local_fields.append(key)

            if len(local_fields) == 1:
                fields.append(local_fields[0])
                idxs_in_order.append(i)
                break

    my_ticket = valid_row_tickets[0:cols]
    ans = 1
    for i in idxs_in_order:
        ans = ans * my_ticket[i]

    return ans


if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')
