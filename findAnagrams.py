"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p = sorted(p)
        
        res = []
        for i in range(0, len(s)-len(p)+1):
            sub = sorted(s[i:i+len(p)])
            if sub == p:
                res.append(i)
                
        return res
                
            