"""
Module for parsing reactor level reports.
"""

def parse_report(line):
    """
    Parse a single report line into a list of levels.
    
    Args:
        line (str): Input line containing level readings
        
    Returns:
        list: List of integer levels
    """
    return [int(x) for x in line.strip().split()]

def parse_reports_file(file_path):
    """
    Parse the entire reports input file.
    
    Args:
        file_path (str): Path to input file
        
    Returns:
        list: List of level reports, where each report is a list of integers
    """
    reports = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                reports.append(parse_report(line))
    except FileNotFoundError:
        print(f"Error: Input file '{file_path}' not found.")
        return []
        
    return reports
