# antenna_collinearity.py

"""
Module for parsing the antenna grid and computing antinode positions.
"""

from itertools import combinations
from math import gcd

def parse_grid(file):
    """
    Parses the input file into a 2D grid.

    Parameters:
    - file: File object to read the grid from.

    Returns:
    - grid: List of lists representing the grid.
    """
    grid = [list(line.rstrip("\n")) for line in file]
    return grid


def group_antennas(grid):
    """
    Groups antenna positions by their frequency.

    Parameters:
    - grid: 2D list representing the grid.

    Returns:
    - freq_dict: Dictionary mapping frequency to a list of (row, col) positions.
    """
    freq_dict = {}
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell.isalnum():  # Check if the cell is a letter or digit
                if cell not in freq_dict:
                    freq_dict[cell] = []
                freq_dict[cell].append((row_idx, col_idx))
    return freq_dict


def get_line_positions(p1, p2):
    """
    Uses Bresenham's Line Algorithm to get all grid positions on the line between p1 and p2.

    Parameters:
    - p1: Tuple (row, col) for the first point.
    - p2: Tuple (row, col) for the second point.

    Returns:
    - positions: List of (row, col) tuples on the line from p1 to p2 inclusive.
    """
    positions = []
    r1, c1 = p1
    r2, c2 = p2

    dr = r2 - r1
    dc = c2 - c1

    step_r = 1 if dr > 0 else -1 if dr < 0 else 0
    step_c = 1 if dc > 0 else -1 if dc < 0 else 0

    dr = abs(dr)
    dc = abs(dc)

    if dc > dr:
        err = dc / 2.0
        while c1 != c2:
            positions.append((r1, c1))
            err -= dr
            if err < 0:
                r1 += step_r
                err += dc
            c1 += step_c
    else:
        err = dr / 2.0
        while r1 != r2:
            positions.append((r1, c1))
            err -= dc
            if err < 0:
                c1 += step_c
                err += dr
            r1 += step_r
    positions.append((r2, c2))  # Include the last point
    return positions


def compute_antinode_positions_part1(freq_dict, rows, cols):
    """
    Computes antinode positions based on Part 1 rules:
    An antinode occurs where one antenna is twice as far as the other in a line.

    Parameters:
    - freq_dict: Dictionary mapping frequency to a list of antenna positions.
    - rows: Total number of rows in the grid.
    - cols: Total number of columns in the grid.

    Returns:
    - antinodes_part1: Set of (row, col) tuples representing antinode positions for Part 1.
    """
    antinodes_part1 = set()

    for freq, positions in freq_dict.items():
        num_antenna = len(positions)
        if num_antenna < 2:
            continue  # Need at least two antennas to form antinodes

        # Iterate through all unique pairs of antennas
        for P, Q in combinations(positions, 2):
            # Calculate the vector from P to Q
            dr = Q[0] - P[0]
            dc = Q[1] - P[1]

            # Calculate antinode positions based on the distance ratio
            # Antinode A: Position beyond Q, same direction
            A_row = Q[0] + dr
            A_col = Q[1] + dc
            if 0 <= A_row < rows and 0 <= A_col < cols:
                antinodes_part1.add((A_row, A_col))

            # Antinode B: Position beyond P, opposite direction
            B_row = P[0] - dr
            B_col = P[1] - dc
            if 0 <= B_row < rows and 0 <= B_col < cols:
                antinodes_part1.add((B_row, B_col))

    return antinodes_part1

def compute_antinode_positions_part2(freq_dict, rows, cols):
    """
    Computes antinode positions based on Part 2 rules:
    An antinode occurs at any grid position exactly in line with at least two antennas of the same frequency.
    This includes the positions of the antennas themselves (unless it's the only antenna of its frequency).

    Parameters:
    - freq_dict: Dictionary mapping frequency to a list of antenna positions.
    - rows: Total number of rows in the grid.
    - cols: Total number of columns in the grid.

    Returns:
    - antinodes_part2: Set of (row, col) tuples representing antinode positions for Part 2.
    """
    antinodes_part2 = set()

    from collections import defaultdict

    line_dict = defaultdict(set)  # Maps line keys to sets of antenna positions

    for freq, positions in freq_dict.items():
        num_antenna = len(positions)
        if num_antenna < 2:
            continue  # Need at least two antennas to form antinodes

        # Identify all unique lines formed by the antennas
        for P, Q in combinations(positions, 2):
            line_key = get_line_key(P, Q)
            line_dict[line_key].update([P, Q])

    # For each unique line that has at least two antennas
    for line_key, antenna_positions in line_dict.items():
        if len(antenna_positions) < 2:
            continue  # Skip lines that don't have at least two antennas

        # Generate all positions along the line within the grid bounds
        positions_on_line = get_positions_on_line(line_key, rows, cols)
        antinodes_part2.update(positions_on_line)

    return antinodes_part2

def get_line_key(p1, p2):
    """
    Computes a canonical representation of the line passing through p1 and p2.
    The line is represented as a tuple (dy/dx, intercept), where dy/dx is the reduced slope.

    Parameters:
    - p1, p2: Tuples (row, col) representing two points.

    Returns:
    - line_key: Tuple representing the line.
    """
    x1, y1 = p1[1], p1[0]
    x2, y2 = p2[1], p2[0]

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        slope = ("inf", 0)
        intercept = x1  # x = intercept
    else:
        # Reduce the slope fraction
        divisor = gcd(dy, dx)
        reduced_dy = dy // divisor
        reduced_dx = dx // divisor
        slope = (reduced_dy, reduced_dx)

        # Compute intercept: y = mx + b => b = y - mx
        # We use the slope and a point to find the intercept
        intercept_numerator = y1 * reduced_dx - reduced_dy * x1
        intercept_denominator = reduced_dx
        # Reduce intercept fraction
        intercept_divisor = gcd(intercept_numerator, intercept_denominator)
        intercept = (
            intercept_numerator // intercept_divisor,
            intercept_denominator // intercept_divisor,
        )

    return (slope, intercept)

def get_positions_on_line(line_key, rows, cols):
    """
    Generates all grid positions along the line within the grid bounds.

    Parameters:
    - line_key: Tuple representing the line.
    - rows: Number of rows in the grid.
    - cols: Number of columns in the grid.

    Returns:
    - positions: Set of (row, col) tuples on the line within the grid bounds.
    """
    positions = set()
    slope, intercept = line_key

    if slope == ("inf", 0):
        # Vertical line x = intercept
        x = intercept
        if 0 <= x < cols:
            for y in range(rows):
                positions.add((y, x))
    else:
        dy, dx = slope
        intercept_numer, intercept_denom = intercept

        for x in range(cols):
            # y = (dy/dx)*x + intercept
            y_numer = dy * x * intercept_denom + intercept_numer * dx
            y_denom = dx * intercept_denom
            if y_denom == 0:
                continue
            if y_numer % y_denom != 0:
                continue  # y is not an integer
            y = y_numer // y_denom
            if 0 <= y < rows:
                positions.add((y, x))

    return positions
