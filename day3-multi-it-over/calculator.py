"""
Module for performing calculations on multiplication instructions.
"""


def calculate_instruction(x, y):
    """
    Calculate the result of a multiplication instruction.

    Args:
        x (int): First number
        y (int): Second number

    Returns:
        int: Product of x and y
    """
    return x * y


def calculate_total(instructions):
    """
    Calculate the sum of all multiplication results.

    Args:
        instructions (list): List of tuples containing number pairs

    Returns:
        int: Sum of all multiplication results
    """
    return sum(calculate_instruction(x, y) for x, y in instructions)
