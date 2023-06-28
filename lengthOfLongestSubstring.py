"""
Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {} 
        i, j, res = 0, 0, 0
        while i < len(s) and j < len(s): 
            if s[j] in map:
                i = max(i, map[s[j]])
            res = max(res, j - i + 1) 
            map[s[j]] = j + 1
            j += 1
        
        return res 
    


