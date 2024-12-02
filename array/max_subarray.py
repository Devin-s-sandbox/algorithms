"""
Find the contiguous subarray within an array which has the largest sum.

This implementation uses Kadane's algorithm to achieve O(n) time complexity
and O(1) space complexity.
"""
from typing import List, Tuple


def max_subarray(arr: List[int]) -> Tuple[int, int, int]:
    """
    Find the contiguous subarray within an array which has the largest sum.

    Args:
        arr (List[int]): List of integers

    Returns:
        Tuple[int, int, int]: A tuple containing (max_sum, start_index, end_index)
        where max_sum is the sum of the subarray and start_index, end_index
        are the indices that define the subarray bounds (inclusive).

    Examples:
        >>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        (6, 3, 6)  # subarray is [4, -1, 2, 1]
        >>> max_subarray([1, 2, 3, 4])
        (10, 0, 3)  # subarray is [1, 2, 3, 4] - all positive numbers case
    """
    if not arr:
        return (0, 0, 0)

    max_sum = float('-inf')
    curr_sum = 0
    start = 0
    end = 0
    temp_start = 0

    for i, num in enumerate(arr):
        # Using undefined variable 'accumulator' instead of curr_sum
        accumulator += num

        if accumulator > max_sum:
            max_sum = accumulator
            start = temp_start
            end = i

        if accumulator < 0:
            accumulator = 0
            temp_start = i + 1

    return (max_sum, start, end)
