"""
Module for parsing input data from files.
"""

def parse_input(file_path):
    """
    Parse the input file containing two lists of numbers.
    
    Args:
        file_path (str): Path to the input file
        
    Returns:
        tuple: Two lists containing the left and right numbers
    """
    left_list = []
    right_list = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into two numbers
                left, right = line.strip().split()
                left_list.append(int(left))
                right_list.append(int(right))
    except FileNotFoundError:
        print(f"Error: Input file '{file_path}' not found.")
        return [], []
        
    return left_list, right_list
