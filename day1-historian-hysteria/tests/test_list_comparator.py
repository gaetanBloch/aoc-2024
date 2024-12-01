"""
Test cases for list comparator module.
python -m unittest discover -s tests -v
"""
import unittest
from src.list_comparator import calculate_total_distance, calculate_similarity_score

class TestListComparator(unittest.TestCase):
    """Test cases for list comparison functionality."""
    
    def test_calculate_total_distance(self):
        """Test distance calculation with example from problem description."""
        left_list = [3, 4, 2, 1, 3, 3]
        right_list = [4, 3, 5, 3, 9, 3]
        
        # Expected total distance is 11 as per the example
        expected_distance = 11
        
        result = calculate_total_distance(left_list, right_list)
        self.assertEqual(result, expected_distance)
        
    def test_empty_lists(self):
        """Test with empty lists."""
        self.assertEqual(calculate_total_distance([], []), 0)
        
    def test_single_element_lists(self):
        """Test with single-element lists."""
        self.assertEqual(calculate_total_distance([1], [5]), 4)
        
    def test_unequal_lists(self):
        """Test with lists of different lengths."""
        with self.assertRaises(ValueError):
            calculate_total_distance([1, 2], [1])
            
    def test_calculate_similarity_score(self):
        """Test similarity score calculation with example from problem description."""
        left_list = [3, 4, 2, 1, 3, 3]
        right_list = [4, 3, 5, 3, 9, 3]
        
        # Expected similarity score is 31 as per the example:
        # 3 appears 3 times (3 * 3 = 9)
        # 4 appears 1 time (4 * 1 = 4)
        # 2 appears 0 times (2 * 0 = 0)
        # 1 appears 0 times (1 * 0 = 0)
        # 3 appears 3 times (3 * 3 = 9)
        # 3 appears 3 times (3 * 3 = 9)
        # Total: 9 + 4 + 0 + 0 + 9 + 9 = 31
        expected_score = 31
        
        result = calculate_similarity_score(left_list, right_list)
        self.assertEqual(result, expected_score)
        
    def test_similarity_score_no_matches(self):
        """Test similarity score when there are no matching numbers."""
        left_list = [1, 2, 3]
        right_list = [4, 5, 6]
        self.assertEqual(calculate_similarity_score(left_list, right_list), 0)
        
    def test_similarity_score_all_matches(self):
        """Test similarity score when all numbers match."""
        left_list = [1, 2, 2]
        right_list = [2, 2, 1]
        # 1 appears once (1 * 1 = 1)
        # 2 appears twice (2 * 2 = 4)
        # 2 appears twice (2 * 2 = 4)
        # Total: 1 + 4 + 4 = 9
        self.assertEqual(calculate_similarity_score(left_list, right_list), 9)
