# main.py

"""
Main application for solving the Resonant Collinearity challenge.
"""

from antenna_collinearity import (
    parse_grid,
    group_antennas,
    compute_antinode_positions_part1,
    compute_antinode_positions_part2,
)


def solve_challenge():
    """
    Main function to solve the Resonant Collinearity challenge.
    """
    print("Day 8: Resonant Collinearity")
    print("----------------------------")

    try:
        with open("input.txt", "r") as file:
            grid = parse_grid(file)
    except FileNotFoundError:
        print("Error: Input file 'input.txt' not found.")
        return

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    freq_dict = group_antennas(grid)

    # Part 1: Antinodes based on distance ratio
    antinodes_part1 = compute_antinode_positions_part1(freq_dict, rows, cols)
    total_antinodes_part1 = len(antinodes_part1)

    # Part 2: Antinodes based on exact collinearity
    antinodes_part2 = compute_antinode_positions_part2(freq_dict, rows, cols)
    total_antinodes_part2 = len(antinodes_part2)

    print(f"\nResults:")
    print(
        f"Part 1 - Total unique antinode locations (distance ratio): {total_antinodes_part1}"
    )
    print(
        f"Part 2 - Total unique antinode locations (exact collinearity): {total_antinodes_part2}"
    )


if __name__ == "__main__":
    solve_challenge()
