"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return [] 
    
        digitmap = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def bt(curr, i, res):
            if i ==len(digits):
                res.append(''.join(curr)) 
                return
            for c in digitmap[int(digits[i])]:
                bt(curr + [c], i+1, res)

        res = [] 
        bt([], 0, res)
        
        return res 