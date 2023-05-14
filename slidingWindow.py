"""
Sliding window
usually used with arrays, avoid repetitive computations and keep some "window" that saves the current state. 

"""

# Given a string s, find the length of the longest substring without repeating characters.

from collections import defaultdict

def lengthOfLongestSubstring(self, s: str) -> int:
    map = defaultdict(int)
    i, j = 0, 0
    maxLength = 0 

    while j < len(s):
        char = s[j] 

        if map[s[j]]: 
            maxLength = max(maxLength, j - i) 
            i = max(i, map[s[j]]+1)
        map[s[j]] += 1

        j += 1
    return max(maxLength, j - i)


print(lengthOfLongestSubstring("abcdefaaebe"))


# given an array of numbers, find the maximum sum of the consecutive k elements 

def maxSum(arr, k):
    n = len(arr)
    
    if n < k:
        return None
 
    # Compute sum of first window of size k
    window_sum = sum(arr[:k])
 
    # first sum available
    max_sum = window_sum

    # iterate through every element here, slide the window of k elements from left to right.
    # check that the sum is greater than the current max sum. if yes, replace max_sum 

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
 
    return max_sum



print(maxSum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4)) # 24



# given an array of numbers, find the subarray with the largest sum

def maxSum(nums):

    maxSum = -999999
    for i in range(0, len(nums)):
        sumSoFar = max(nums[i], nums[i] + sumSoFar)
        maxSum = max(sumSoFar, maxSum) 

    return maxSum
 

