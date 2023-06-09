"""
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
"""

from typing import List
from collections import defaultdict


# need to figure out the association between letters of each word and hash these.
# fortunately, we can keep a list of differences between indices of ascii values in the format () i.e. (1,1,1) -> abc, cde
# we can use a map to store them. Essentially hashing the values
class Solution: 
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = {}
        for s in strings: 
            pattern = ()
            for i in range(1, len(s)): 
                pattern += pattern + ((ord(s[i]) - ord(s[i-1]) + 26) % 26,)
            if pattern not in groups:
                groups[pattern] = []
            groups[pattern].append(s)
        
        return groups.values() 

sol = Solution()

print(sol.groupStrings(["abc","cde","aef", "bfg"]))