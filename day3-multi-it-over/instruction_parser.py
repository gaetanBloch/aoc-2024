"""
Module for parsing multiplication instructions from corrupted memory.
"""

import re


def parse_instruction(text):
    """
    Parse a single multiplication instruction from text.
    Valid format: mul(X,Y) where X and Y are 1-3 digit numbers.

    Args:
        text (str): Text containing potential instruction

    Returns:
        tuple: Pair of numbers to multiply, or None if invalid
    """
    # Match exactly 'mul(' followed by 1-3 digits, comma, 1-3 digits, and ')'
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    match = re.match(pattern, text)

    if match:
        x, y = match.groups()
        return int(x), int(y)
    return None


def find_valid_instructions(memory):
    """
    Find all valid multiplication instructions in corrupted memory.

    Args:
        memory (str): Corrupted memory contents

    Returns:
        list: List of tuples containing pairs of numbers to multiply
    """
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    potential_instructions = re.finditer(pattern, memory)

    instructions = []
    for match in potential_instructions:
        instruction = parse_instruction(match.group())
        if instruction:
            instructions.append(instruction)

    return instructions
