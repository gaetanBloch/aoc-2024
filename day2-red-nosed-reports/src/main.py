"""
Main application for solving the Red-Nosed Reports challenge.
"""
from report_parser import parse_reports_file
from report_validator import count_safe_reports

def solve_challenge():
    """
    Main function to solve the Red-Nosed Reports challenge.
    """
    print("Day 2: Red-Nosed Reports")
    print("-----------------------")
    
    # Parse input file
    reports = parse_reports_file('input.txt')
    
    if not reports:
        return
    
    # Part 1: Count safe reports without dampener
    safe_count = count_safe_reports(reports)
    
    # Part 2: Count safe reports with Problem Dampener
    safe_count_with_dampener = count_safe_reports(reports, use_dampener=True)
    
    print(f"\nResults:")
    print(f"Part 1 - Number of safe reports: {safe_count}")
    print(f"Part 2 - Number of safe reports with Problem Dampener: {safe_count_with_dampener}")

if __name__ == "__main__":
    solve_challenge()
