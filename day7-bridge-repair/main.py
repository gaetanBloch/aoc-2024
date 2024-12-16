"""
Main application for solving the Bridge Repair challenge.
"""

from calibration import parse_input, find_valid_equations


def solve_challenge():
    """
    Main function to solve the Bridge Repair challenge.
    """
    print("Day 7: Bridge Repair")
    print("--------------------")

    try:
        with open("input.txt", "r") as file:
            equations = parse_input(file)
    except FileNotFoundError:
        print("Error: Input file 'input.txt' not found.")
        return

    # Part 1: Only addition and multiplication
    valid_test_values_part1 = find_valid_equations(equations, use_concat=False)
    total_calibration_part1 = sum(valid_test_values_part1)

    # Part 2: All operators including concatenation
    valid_test_values_part2 = find_valid_equations(equations, use_concat=True)
    total_calibration_part2 = sum(valid_test_values_part2)

    print(f"\nResults:")
    print(f"Part 1 - Total calibration (+ and * only): {total_calibration_part1}")
    print(f"Part 2 - Total calibration (all operators): {total_calibration_part2}")


if __name__ == "__main__":
    solve_challenge()
