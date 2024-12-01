"""
Main application for solving the Historian Hysteria challenge.
"""
from input_parser import parse_input
from list_comparator import calculate_total_distance

def solve_challenge():
    """
    Main function to solve the Historian Hysteria challenge.
    """
    print("Day 1: Historian Hysteria")
    print("-------------------------")
    
    # Parse input file
    left_list, right_list = parse_input('./input.txt')
    
    if not left_list or not right_list:
        return
    
    # Calculate total distance
    total_distance = calculate_total_distance(left_list, right_list)
    
    print(f"\nResults:")
    print(f"Total distance between the lists: {total_distance}")
    
if __name__ == "__main__":
    solve_challenge()
