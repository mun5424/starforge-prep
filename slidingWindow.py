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
