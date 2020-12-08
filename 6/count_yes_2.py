"""
File: count_yes_2.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: count yes answers, part2
"""

import fileinput


def process(data):
    if '' in data:
        data.remove('')

    for i, ans in enumerate(data):
        if i == 0:
            prev = set(list(ans))
            continue

        curr = set(list(ans))
        prev = curr.intersection(prev)

    num_common = len(prev)
    return num_common


form_ans = []
ans = 0
for i, line in enumerate(fileinput.input('./input.txt')):
    form_ans.append(line.rstrip())
    if line == '\n':
        ans = ans + process(form_ans)
        form_ans = []

if len(form_ans):
    ans = ans + process(form_ans)

print(f'Answer: {ans}')
