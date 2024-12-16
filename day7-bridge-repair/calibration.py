"""
Module for parsing and evaluating calibration equations.
"""

from itertools import product


def parse_input(file):
    """
    Parses the input file into a list of equations.
    Each equation is a tuple containing the test value and a list of numbers.
    """
    equations = []
    for line in file:
        line = line.strip()
        if not line:
            continue
        if ":" in line:
            test_value_str, numbers_str = line.split(":")
            test_value = int(test_value_str.strip())
            numbers = list(map(int, numbers_str.strip().split()))
            equations.append((test_value, numbers))
    return equations


def generate_operator_combinations(num_count, use_concat=False):
    """
    Generates all possible combinations of operators for a given number of operators (num_count - 1).
    Includes '||' operator if use_concat is True.
    """
    if use_concat:
        operators = ["+", "*", "||"]
    else:
        operators = ["+", "*"]
    return product(operators, repeat=num_count - 1)


def concatenate_numbers(a, b):
    """
    Concatenates two numbers together.
    Example: concatenate_numbers(12, 345) = 12345
    """
    return int(str(a) + str(b))


def evaluate_expression(numbers, operators):
    """
    Evaluates the expression formed by the numbers and operators
    left-to-right without respecting the standard operator precedence.
    """
    result = numbers[0]
    for op, num in zip(operators, numbers[1:]):
        if op == "+":
            result += num
        elif op == "*":
            result *= num
        elif op == "||":
            result = concatenate_numbers(result, num)
    return result


def find_valid_equations(equations, use_concat=False):
    """
    Finds all equations that can be made true by inserting operators
    between the numbers to produce the test value.
    Returns a list of the valid test values.

    Parameters:
    - equations: List of tuples, each containing (test_value, [numbers])
    - use_concat: Boolean indicating whether to include the '||' operator
    """
    valid_test_values = []

    for test_value, numbers in equations:
        num_count = len(numbers)
        operator_combinations = generate_operator_combinations(num_count, use_concat)
        found = False

        for operators in operator_combinations:
            result = evaluate_expression(numbers, operators)
            if result == test_value:
                found = True
                break  # No need to check other combinations for this equation

        if found:
            valid_test_values.append(test_value)

    return valid_test_values
