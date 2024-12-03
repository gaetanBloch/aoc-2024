"""
Main application for solving the Mull It Over challenge.
"""

from instruction_parser import find_valid_instructions, get_enabled_instructions
from calculator import calculate_total


def solve_challenge():
    """
    Main function to solve the Mull It Over challenge.
    """
    print("Day 3: Mull It Over")
    print("------------------")

    try:
        with open("input.txt", "r") as file:
            memory = file.read().strip()
    except FileNotFoundError:
        print("Error: Input file 'input.txt' not found.")
        return

    # Find all instructions
    instructions = find_valid_instructions(memory)

    # Part 1: Calculate total of all multiplication results
    part1_instructions = [
        (i.numbers[0], i.numbers[1])
        for i in instructions
        if i.type == "mul" and i.numbers
    ]
    total_part1 = calculate_total(part1_instructions)

    # Part 2: Calculate total of enabled multiplication results
    enabled_instructions = get_enabled_instructions(instructions)
    total_part2 = calculate_total(enabled_instructions)

    print(f"\nResults:")
    print(f"Part 1 - Sum of all multiplication results: {total_part1}")
    print(f"Part 2 - Sum of enabled multiplication results: {total_part2}")


if __name__ == "__main__":
    solve_challenge()
