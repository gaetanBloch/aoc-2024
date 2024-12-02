"""
Module for validating reactor level reports.
"""

def is_monotonic(levels):
    """
    Check if levels are either all increasing or all decreasing.
    
    Args:
        levels (list): List of level readings
        
    Returns:
        bool: True if levels are monotonic, False otherwise
    """
    increasing = decreasing = True
    
    for i in range(1, len(levels)):
        if levels[i] <= levels[i-1]:
            increasing = False
        if levels[i] >= levels[i-1]:
            decreasing = False
            
    return increasing or decreasing

def has_valid_differences(levels):
    """
    Check if adjacent level differences are between 1 and 3 inclusive.
    
    Args:
        levels (list): List of level readings
        
    Returns:
        bool: True if differences are valid, False otherwise
    """
    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i-1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_report_safe(levels):
    """
    Check if a report is safe according to all rules.
    
    Args:
        levels (list): List of level readings
        
    Returns:
        bool: True if the report is safe, False otherwise
    """
    return is_monotonic(levels) and has_valid_differences(levels)

def count_safe_reports(reports):
    """
    Count the number of safe reports.
    
    Args:
        reports (list): List of reports to check
        
    Returns:
        int: Number of safe reports
    """
    return sum(1 for report in reports if is_report_safe(report))
