"""
Module for parsing multiplication instructions from corrupted memory.
"""

import re
from dataclasses import dataclass
from typing import Optional, List, Tuple


@dataclass
class Instruction:
    """Represents a parsed instruction with its position in memory."""

    type: str  # 'mul', 'do', or 'don't'
    position: int
    numbers: Optional[Tuple[int, int]] = None


def parse_instruction(text: str, position: int) -> Optional[Instruction]:
    """
    Parse a single instruction from text.

    Args:
        text (str): Text containing potential instruction
        position (int): Position of instruction in memory

    Returns:
        Optional[Instruction]: Parsed instruction or None if invalid
    """
    # Check for do() and don't() instructions
    if text == "do()":
        return Instruction(type="do", position=position)
    if text == "don't()":
        return Instruction(type="don't", position=position)

    # Check for multiplication instruction
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    match = re.match(mul_pattern, text)

    if match:
        x, y = map(int, match.groups())
        return Instruction(type="mul", position=position, numbers=(x, y))

    return None


def find_valid_instructions(memory: str) -> List[Instruction]:
    """
    Find all valid instructions in corrupted memory.

    Args:
        memory (str): Corrupted memory contents

    Returns:
        List[Instruction]: List of parsed instructions in order of appearance
    """
    # Find all potential instructions
    patterns = [
        r"mul\(\d{1,3},\d{1,3}\)",  # multiplication
        r"do\(\)",  # enable
        r"don't\(\)",  # disable
    ]

    instructions = []

    # Find all matches for each pattern
    for pattern in patterns:
        for match in re.finditer(pattern, memory):
            instruction = parse_instruction(match.group(), match.start())
            if instruction:
                instructions.append(instruction)

    # Sort instructions by position to maintain order
    return sorted(instructions, key=lambda x: x.position)


def get_enabled_instructions(instructions: List[Instruction]) -> List[Tuple[int, int]]:
    """
    Filter instructions based on do() and don't() conditions.

    Args:
        instructions (List[Instruction]): List of all parsed instructions

    Returns:
        List[Tuple[int, int]]: List of number pairs from enabled mul instructions
    """
    enabled = True  # Instructions are enabled by default
    enabled_muls = []

    for instruction in instructions:
        if instruction.type == "do":
            enabled = True
        elif instruction.type == "don't":
            enabled = False
        elif instruction.type == "mul" and enabled and instruction.numbers:
            enabled_muls.append(instruction.numbers)

    return enabled_muls
