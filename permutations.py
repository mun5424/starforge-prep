"""
permutations

return all possible permutations of a certain array combination or a string

"""



# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    res = [] 
    visited = set()

    def bt(current, idx):
        if len(current) == len(nums): 
            res.append(current)
            return 

        for i in range(len(nums)):
            if i not in visited: 
                visited.add(i)
                bt(current + [nums[i]], idx + 1)
                visited.remove(i)
    
    bt([], 0)

permute([1,2,3]) 
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

