"""
File: sum_2020.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description:find sum of two numbers = 2020
"""

import fileinput

list_of_numbers = []


def find_pairs(numbers, final_sum=2020):
    pairs_prod = -1
    for num in numbers:
        diff = final_sum - num
        if diff in list_of_numbers and diff > 0:
            pairs_prod = diff * num
            break

    return pairs_prod, (num, diff)


def find_triplets(numbers, final_sum=2020):
    final_sum = 2020
    tmp_numbers = numbers.copy()
    for i, num in enumerate(numbers):
        diff = final_sum - num
        tmp_numbers.pop(i)
        prod, pair = find_pairs(tmp_numbers, final_sum=diff)
        if prod == -1:
            tmp_numbers = numbers.copy()
        else:
            prod = prod * num
            print(f'Product: {prod}, Triplet: {num, pair}')
            break

    return prod


for line in fileinput.input('./input.txt'):
    number = int(line.strip())
    list_of_numbers.append(number)

print(find_pairs(list_of_numbers))
print(find_triplets(list_of_numbers))
