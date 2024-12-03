"""
Main application for solving the Mull It Over challenge.
"""

from instruction_parser import find_valid_instructions
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

    # Find all valid multiplication instructions
    instructions = find_valid_instructions(memory)

    # Calculate total of all multiplication results
    total = calculate_total(instructions)

    print(f"\nResults:")
    print(f"Sum of all multiplication results: {total}")


if __name__ == "__main__":
    solve_challenge()
