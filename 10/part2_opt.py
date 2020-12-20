import fileinput

from collections import defaultdict


def get_list_nums(input_txt):
    list_of_nums = []
    for line in fileinput.input(input_txt):
        num = int(line.rstrip())
        list_of_nums.append(num)

    return list_of_nums


counts = defaultdict(int, {0: 1})

if __name__ == "__main__":
    adapters = get_list_nums('./input.txt')
    adapters = sorted(adapters)

    for a in adapters:
        counts[a] = counts[a - 3] + counts[a -2] + counts[a - 1]

    print(f'Answer: {counts[adapters[-1]]}')
