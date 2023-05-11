# given a set of numbers check if it sums to a certain number 

from typing import List
# given a set of numbers, check if it sums to a certain number 
# each item can be used infinite numbers of times     

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = [] 
    def dfs(path, idx, target):
        if target == 0:
            res.append(path) 
        if target < 0:
            return 
        
        for i in range(idx, len(candidates)): 
            dfs(path + [candidates[i]], i, target - candidates[i])
    
    dfs([], 0, target) 
    return res 





# given a set of numbers, check if it sums to a certain number 
# each item can only be used once
# runtime is O(2^n))
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res = [] 
    candidates.sort()

    # depth first approach where we simulate 
    # python lets you include a list as part of the argument like {currentList + [someInt]}
    # otherwise, we would have to add the item, then subtract the item
    def dfs(idx, path, cur):

        if cur > target:
            return 
        if cur == target:
            res.append(path) 
            return 
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            dfs(i+ 1, path + [candidates[i]], cur + candidates[i])
    
    dfs(0, [], 0)
    return res


# find a combination of numbers that sums up to n such that 
# Only numbers 1 through 9 are used.
# Each number is used at most once.
def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    res = [] 

    nums = [1,2,3,4,5,6,7,8,9]

    def dfs(idx, path, target, k):
        if k < 0 or target < 0:
            return

        if k == 0 and target == 0: 
            res.append(path)
            return 


        for i in range(idx, len(nums)):
            dfs(i + 1, path +[nums[i]], target - nums[i], k - 1)
    dfs(0, [], n, k) 

    return res
