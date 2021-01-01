"""
File: part1.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: sum of all the expressions
"""


import fileinput


def mul(a, b):
    return a * b


def sum(a, b):
    return a + b


def find_parentheses(line):
    open_pos = []
    pairs = []
    for i, char in enumerate(line):
        if char == '(':
            open_pos.append(i)
        elif char == ')':
            pairs.append((open_pos.pop(), i))

    return pairs


def get_operand_b(expression):
    operand = ''
    for i, char in enumerate(expression):
        if char == '*' or char == '+':
            break
        operand = operand + char

    return int(operand), i


def evaluate(expression):
    run = True
    while run:
        try:
            val = int(expression)
            run = False
        except ValueError:
            for i, char in enumerate(expression):
                if char == '*':
                    a = int(expression[0:i])
                    b, j = get_operand_b(expression[i + 1:])
                    result = (a * b)
                    expression = str(result) + expression[i + 1 + j:]
                    run = True
                    break

                if char == '+':
                    a = int(expression[0:i])
                    b, j = get_operand_b(expression[i + 1:])
                    result = (a + b)
                    expression = str(result) + expression[i + 1 + j:]
                    run = True
                    break

    return result


def main(input_file):
    total = 0
    for line in fileinput.input(input_file):
        line = line.rstrip()
        line = line.replace(' ', '')
        run = True
        while run:
            if '(' in line:
                pairs = find_parentheses(line)
                for i, j in pairs:
                    expression = line[i + 1:j]
                    result = evaluate(expression)
                    line = line[0:i] + str(result) + line[j + 1:]
                    break
            else:
                run = False

        total = total + evaluate(line)

    return total


if __name__ == "__main__":
    ans = main('./input.txt')
    print(f'Answer: {ans}')
