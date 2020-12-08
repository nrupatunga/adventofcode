"""
File: count_yes.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: count yes answers
"""

import fileinput


def process(data):
    new_data = ''.join(string for string in data)
    new_data = new_data.rstrip()
    num_q_yes = len(set(list(new_data)))

    return num_q_yes


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
