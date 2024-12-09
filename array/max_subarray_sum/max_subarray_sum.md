Given an array of integers and a window size k, find the maximum sum of any contiguous subarray of size k.

For example:
Given array = [1, 4, 2, 10, 2, 3, 1, 0, 20] and k = 4
return 24 (sum of subarray [2, 10, 2, 3])

This problem demonstrates the sliding window technique for efficient array traversal.
The solution maintains a window of size k and slides it through the array,
keeping track of the maximum sum encountered.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) as we only use a constant amount of extra space
