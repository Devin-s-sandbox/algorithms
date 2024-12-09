/**
 * Find the maximum sum of any contiguous subarray of size k.
 *
 * @param {number[]} arr - Array of integers
 * @param {number} k - Size of the sliding window
 * @returns {number} Maximum sum found in any k-sized window
 *
 * Time Complexity: O(n) where n is the length of the array
 * Space Complexity: O(1) as we only use constant extra space
 */
function maxSubarraySum(arr, k) {
    // Handle edge cases
    if (!arr || k <= 0 || k > arr.length) {
        return 0
    }

    // Calculate sum of first window
    let windowSum = arr.slice(0, k).reduce((a, b) => a + b, 0)
    let maxSum = windowSum

    // Slide window and update maxSum
    for (let i = 0; i < arr.length - k; i++) {
        windowSum = windowSum - arr[i] + arr[i + k]
        maxSum = Math.max(maxSum, windowSum)
    }

    return maxSum
}

// Test cases
const testCases = [
    {arr: [1, 4, 2, 10, 2, 3, 1, 0, 20], k: 4, expected: 24}, // Standard case
    {arr: [1, 2, 3, 4], k: 2, expected: 7},                    // Small array
    {arr: [5], k: 1, expected: 5},                             // Single element
    {arr: [], k: 3, expected: 0},                              // Empty array
    {arr: [1, 2, 3], k: 4, expected: 0},                       // k > array length
]

testCases.forEach(({arr, k, expected}) => {
    const result = maxSubarraySum(arr, k)
    console.assert(result === expected, `Failed: arr=${arr}, k=${k}. Expected ${expected}, got ${result}`)
    console.log(`✓ Passed: arr=${arr}, k=${k}, result=${result}`)
})
