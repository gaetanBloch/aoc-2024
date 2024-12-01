"""
Main application for solving the Historian Hysteria challenge.
"""
from input_parser import parse_input
from list_comparator import calculate_total_distance, calculate_similarity_score

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
    
    # Part 1: Calculate total distance
    total_distance = calculate_total_distance(left_list, right_list)
    
    # Part 2: Calculate similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    
    print(f"\nResults:")
    print(f"Part 1 - Total distance between the lists: {total_distance}")
    print(f"Part 2 - Similarity score between the lists: {similarity_score}")

if __name__ == "__main__":
    solve_challenge()
