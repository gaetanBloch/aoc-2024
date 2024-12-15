"""
Module for counting occurrences of words in a grid.
"""


def count_occurrences(grid, word):
    """
    Counts all occurrences of the word in the grid in all 8 directions.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Directions: N, NE, E, SE, S, SW, W, NW
    directions = [
        (-1, 0),  # N
        (-1, 1),  # NE
        (0, 1),  # E
        (1, 1),  # SE
        (1, 0),  # S
        (1, -1),  # SW
        (0, -1),  # W
        (-1, -1),  # NW
    ]

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if check_word(grid, word, row, col, dr, dc):
                    count += 1

    return count


def check_word(grid, word, row, col, dr, dc):
    """
    Checks if the word exists starting from (row, col) in direction (dr, dc).
    """
    for i in range(len(word)):
        r = row + dr * i
        c = col + dc * i
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return False
        if grid[r][c] != word[i]:
            return False
    return True


def count_x_mas_occurrences(grid):
    """
    Counts all occurrences of the X-MAS pattern in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Possible combinations of 'MAS' and 'SAM' for each diagonal
    diagonals = [("MAS", "MAS"), ("MAS", "SAM"), ("SAM", "MAS"), ("SAM", "SAM")]

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            for diag1, diag2 in diagonals:
                if check_x_mas_pattern(grid, row, col, diag1, diag2):
                    count += 1

    return count


def check_x_mas_pattern(grid, row, col, diag1, diag2):
    """
    Checks if the X-MAS pattern exists centered at (row, col) with given diagonals.
    """
    # Offsets for diagonals
    offsets = [(-1, -1), (0, 0), (1, 1)]  # NW to SE
    for i, (dr, dc) in enumerate(offsets):
        r = row + dr
        c = col + dc
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            return False
        if grid[r][c] != diag1[i]:
            return False

    offsets = [(-1, 1), (0, 0), (1, -1)]  # NE to SW
    for i, (dr, dc) in enumerate(offsets):
        r = row + dr
        c = col + dc
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            return False
        if grid[r][c] != diag2[i]:
            return False

    return True
