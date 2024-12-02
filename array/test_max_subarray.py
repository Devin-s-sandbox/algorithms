"""Unit tests for max_subarray algorithm."""
import unittest
from max_subarray import max_subarray


class TestMaxSubarray(unittest.TestCase):
    def test_basic(self):
        """Test basic case with mixed positive and negative numbers."""
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray(arr), (6, 3, 6))

    def test_empty(self):
        """Test empty array case."""
        self.assertEqual(max_subarray([]), (0, 0, 0))

    def test_all_negative(self):
        """Test case where all numbers are negative."""
        arr = [-1, -2, -3, -4]
        self.assertEqual(max_subarray(arr), (-1, 0, 0))

    def test_all_positive(self):
        """Test case where all numbers are positive."""
        arr = [1, 2, 3, 4]
        self.assertEqual(max_subarray(arr), (10, 0, 3))

    def test_single_element(self):
        """Test case with a single element."""
        self.assertEqual(max_subarray([5]), (5, 0, 0))
        self.assertEqual(max_subarray([-5]), (-5, 0, 0))

    def test_two_elements(self):
        """Test case with two elements."""
        self.assertEqual(max_subarray([1, 2]), (3, 0, 1))
        self.assertEqual(max_subarray([-1, 2]), (2, 1, 1))


if __name__ == '__main__':
    unittest.main()
