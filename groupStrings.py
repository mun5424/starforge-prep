"""
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
"""

from collections import defaultdict
from typing import List


# need to figure out the association between letters of each word and hash these.
# fortunately, we can keep a list of differences between indices of ascii values in the format () i.e. (1,1,1) -> abc, cde
# we can use a map to store them. Essentially hashing the values
def groupStrings(strings: List[str]) -> List[List[str]]:
    groups = defaultdict(List) 
    for s in strings: 
        pattern = () 
        for i in range(1, len(s)): 
            pattern += pattern + ((ord(s[i]) - ord(s[i-1]) + 26) % 26,)
        groups[pattern].append(s)
    
    return groups.values() 

