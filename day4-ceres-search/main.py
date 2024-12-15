"""
Main application for solving the Ceres Search challenge.
"""

from counter import count_occurrences, count_x_mas_occurrences


def solve_challenge():
    """
    Main function to solve the Ceres Search challenge.
    """
    print("Day 4: Ceres Search")
    print("-------------------")

    try:
        with open("input.txt", "r") as file:
            grid = [list(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: Input file 'input.txt' not found.")
        return

    # Part 1: Count occurrences of 'XMAS'
    total_occurrences = count_occurrences(grid, "XMAS")
    print(f"\nPart 1 Result:")
    print(f"The word 'XMAS' appears {total_occurrences} times in the word search.")

    # Part 2: Count occurrences of 'X-MAS' pattern
    x_mas_occurrences = count_x_mas_occurrences(grid)
    print(f"\nPart 2 Result:")
    print(f"The 'X-MAS' pattern appears {x_mas_occurrences} times in the word search.")


if __name__ == "__main__":
    solve_challenge()
