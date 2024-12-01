"""
Module for comparing lists and calculating distances between them.
"""

def calculate_total_distance(left_list, right_list):
    """
    Calculate the total distance between two lists by pairing sorted numbers.
    
    Args:
        left_list (list): First list of numbers
        right_list (list): Second list of numbers
        
    Returns:
        int: Total distance between paired numbers
    """
    if len(left_list) != len(right_list):
        raise ValueError("Lists must have the same length")
        
    # Sort both lists to pair smallest with smallest, etc.
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    
    total_distance = 0
    
    # Calculate distance between each pair of numbers
    for left, right in zip(sorted_left, sorted_right):
        distance = abs(left - right)
        total_distance += distance
        
    return total_distance
