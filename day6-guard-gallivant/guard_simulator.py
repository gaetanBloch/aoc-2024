# guard_simulator.py

"""
Module for simulating the guard's movement and finding obstruction positions.
"""


def simulate_guard(grid):
    """
    Simulates the guard's movement and returns the set of positions visited.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = set()

    # Direction vectors: N, E, S, W
    directions = {
        "^": (-1, 0),  # Up
        ">": (0, 1),  # Right
        "v": (1, 0),  # Down
        "<": (0, -1),  # Left
    }
    turn_order = ["^", ">", "v", "<"]  # Order for turning right

    # Find the guard's starting position and direction
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                row, col = r, c
                facing = grid[r][c]
                break
        else:
            continue
        break
    else:
        return visited  # Guard's starting position not found

    # Keep track of visited states to detect loops
    states = set()

    while True:
        visited.add((row, col))
        state = (row, col, facing)
        if state in states:
            # Loop detected
            break
        states.add(state)

        dr, dc = directions[facing]
        next_row, next_col = row + dr, col + dc

        # Check next position
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            # Guard moves off the map
            break
        elif grid[next_row][next_col] == "#":
            # Obstacle ahead, turn right
            idx = turn_order.index(facing)
            facing = turn_order[(idx + 1) % 4]
        else:
            # Move forward
            row, col = next_row, next_col

    return visited


def does_guard_loop(grid):
    """
    Checks if the guard gets stuck in a loop with the given grid.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Direction vectors and turn order as before
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    turn_order = ["^", ">", "v", "<"]

    # Find guard's starting position and direction
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                row, col = r, c
                facing = grid[r][c]
                break
        else:
            continue
        break
    else:
        return False  # Guard's starting position not found

    states = set()

    while True:
        state = (row, col, facing)
        if state in states:
            # Loop detected
            return True
        states.add(state)

        dr, dc = directions[facing]
        next_row, next_col = row + dr, col + dc

        # Check next position
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            # Guard moves off the map
            return False
        elif grid[next_row][next_col] == "#":
            # Obstacle ahead, turn right
            idx = turn_order.index(facing)
            facing = turn_order[(idx + 1) % 4]
        else:
            # Move forward
            row, col = next_row, next_col


def find_obstruction_positions(grid):
    """
    Finds all positions where adding an obstruction causes the guard to loop.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    possible_positions = []

    # Copy of the grid to modify
    import copy

    original_grid = copy.deepcopy(grid)

    # Find guard's starting position
    guard_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ("^", ">", "v", "<"):
                guard_pos = (r, c)
                break
        if guard_pos:
            break

    # Iterate over all positions
    for r in range(rows):
        for c in range(cols):
            if (r, c) == guard_pos:
                continue
            if grid[r][c] != ".":
                continue
            # Place obstruction
            grid[r][c] = "#"
            if does_guard_loop(grid):
                possible_positions.append((r, c))
            # Remove obstruction
            grid[r][c] = "."

    return possible_positions
