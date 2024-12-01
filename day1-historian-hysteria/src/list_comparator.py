"""
Module for comparing lists and calculating distances and similarities between them.
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

def calculate_similarity_score(left_list, right_list):
    """
    Calculate the similarity score between two lists.
    The score is calculated by multiplying each number in the left list
    by the number of times it appears in the right list.
    
    Args:
        left_list (list): First list of numbers
        right_list (list): Second list of numbers
        
    Returns:
        int: Total similarity score
    """
    # Create a frequency map for the right list
    right_frequencies = {}
    for num in right_list:
        right_frequencies[num] = right_frequencies.get(num, 0) + 1
    
    total_score = 0
    
    # Calculate score for each number in left list
    for num in left_list:
        # Multiply the number by its frequency in right list (0 if not present)
        frequency = right_frequencies.get(num, 0)
        total_score += num * frequency
    
    return total_score
