"""
Main application for solving the Print Queue challenge.
"""

from queue_checker import parse_input, is_correct_order, get_middle_page, reorder_update


def solve_challenge():
    """
    Main function to solve the Print Queue challenge.
    """
    print("Day 5: Print Queue")
    print("------------------")

    try:
        with open("input.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: Input file 'input.txt' not found.")
        return

    # Parse ordering rules and updates
    ordering_rules, updates = parse_input(content)

    # Process updates
    total_middle_pages_part1 = 0
    total_middle_pages_part2 = 0
    for update in updates:
        if is_correct_order(update, ordering_rules):
            middle_page = get_middle_page(update)
            total_middle_pages_part1 += middle_page
        else:
            # Reorder the update
            reordered_update = reorder_update(update, ordering_rules)
            middle_page = get_middle_page(reordered_update)
            total_middle_pages_part2 += middle_page

    print(f"\nPart 1 Result:")
    print(
        f"The sum of middle page numbers of correctly-ordered updates is: {total_middle_pages_part1}"
    )

    print(f"\nPart 2 Result:")
    print(
        f"The sum of middle page numbers after reordering incorrect updates is: {total_middle_pages_part2}"
    )


if __name__ == "__main__":
    solve_challenge()
