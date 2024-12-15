# main.py

"""
Main application for solving the Guard Gallivant challenge.
"""

from guard_simulator import simulate_guard, find_obstruction_positions


def solve_challenge():
    """
    Main function to solve the Guard Gallivant challenge.
    """
    print("Day 6: Guard Gallivant")
    print("----------------------")

    try:
        with open("input.txt", "r") as file:
            grid = [list(line.rstrip("\n")) for line in file]
    except FileNotFoundError:
        print("Error: Input file 'input.txt' not found.")
        return

    # Part 1: Simulate guard movement
    visited_positions = simulate_guard(grid)
    total_visited = len(visited_positions)
    print(f"\nPart 1 Result:")
    print(
        f"The guard visited {total_visited} distinct positions before leaving the map."
    )

    # Part 2: Find obstruction positions
    obstruction_positions = find_obstruction_positions(grid)
    total_obstructions = len(obstruction_positions)
    print(f"\nPart 2 Result:")
    print(f"There are {total_obstructions} possible obstruction positions.")


if __name__ == "__main__":
    solve_challenge()
