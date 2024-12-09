from typing import List


def max_subarray_sum(arr: List[int], k: int) -> int:
    """
    Find the maximum sum of any contiguous subarray of size k.

    Args:
        arr: List of integers
        k: Size of the sliding window

    Returns:
        Maximum sum found in any k-sized window

    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(1) as we only use constant extra space
    """
    # Handle edge cases
    if not arr or k <= 0 or k > len(arr):
        return 0

    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide window and update max_sum
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 4, 2, 10, 2, 3, 1, 0, 20], 4, 24),  # Standard case
        ([1, 2, 3, 4], 2, 7),                     # Small array
        ([5], 1, 5),                              # Single element
        ([], 3, 0),                               # Empty array
        ([1, 2, 3], 4, 0),                        # k > array length
    ]

    for arr, k, expected in test_cases:
        result = max_subarray_sum(arr, k)
        assert result == expected, f"Failed: arr={arr}, k={k}. Expected {expected}, got {result}"
        print(f"✓ Passed: arr={arr}, k={k}, result={result}")
