"""
Module for checking update orderings and processing input.
"""


def parse_input(content):
    """
    Parses the input content into ordering rules and updates.
    """
    lines = [line.strip() for line in content.strip().splitlines()]
    ordering_rules = []
    updates = []
    parsing_updates = False

    for line in lines:
        if "|" in line and not parsing_updates:
            # Ordering rule
            x, y = map(int, line.split("|"))
            ordering_rules.append((x, y))
        elif "," in line:
            # Updates
            parsing_updates = True
            update = list(map(int, line.strip().split(",")))
            updates.append(update)
        else:
            continue

    return ordering_rules, updates


def is_correct_order(update, ordering_rules):
    """
    Checks if the update is in the correct order according to the applicable ordering rules.
    """
    positions = {page: idx for idx, page in enumerate(update)}
    applicable_rules = [
        (x, y) for x, y in ordering_rules if x in positions and y in positions
    ]

    for x, y in applicable_rules:
        if positions[x] >= positions[y]:
            return False
    return True


def get_middle_page(update):
    """
    Returns the middle page number of the update.
    """
    mid_index = len(update) // 2
    return update[mid_index]


def reorder_update(update, ordering_rules):
    """
    Reorders the update according to the applicable ordering rules.
    """
    from collections import defaultdict, deque

    # Build graph
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    positions = set(update)

    applicable_rules = [
        (x, y) for x, y in ordering_rules if x in positions and y in positions
    ]

    for page in update:
        in_degree[page] = 0  # Initialize in-degree

    for x, y in applicable_rules:
        graph[x].add(y)
        in_degree[y] += 1

    # Kahn's algorithm for topological sort
    queue = deque([page for page in update if in_degree[page] == 0])
    ordered = []

    while queue:
        page = queue.popleft()
        ordered.append(page)
        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(ordered) != len(update):
        raise ValueError("Cycle detected, cannot reorder update")

    return ordered
