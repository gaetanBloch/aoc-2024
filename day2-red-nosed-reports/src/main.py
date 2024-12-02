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
    
    # Count safe reports
    safe_count = count_safe_reports(reports)
    
    print(f"\nResults:")
    print(f"Number of safe reports: {safe_count}")

if __name__ == "__main__":
    solve_challenge()
