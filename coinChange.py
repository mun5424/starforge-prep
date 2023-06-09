"""
Coin change problem. Lots of variations

Given a set of coins, determine 
1. how many ways it can reach a sum n 
2. minimum number of coins to make n

"""

# find the number of unique ways it can reach a sum n
import sys


def coinChangeWays(coins, n): 
    # dynamic programming approach 
    
    # this assumes that its possible to have multiple uses of the same coin
    # dp array is +1 because we have a 0 base case
    dp = [0] * (n+1) 

    # when there is no sum - there is exactly 1 way of dispensing coins
    dp[0] = 1

    # for every sum j, we simulate subtracting a coin (coin[i])
    # dp[j - coins[i]] => this yields how many ways if the coin was subtracted from the sum.
    # consequently, after adding all of the possible ways, dp[j] will include all the ways up to that sum 
    for i in range(0, len(coins)):
        for j in range(coins[i], n+1): 
            dp[j] += dp[j - coins[i]]     
        return dp[n] 


# find minimum number of coins to reach a target n given a set of coins
# take 1. Greedy Approach 
def greedyMinCoins(coins, target):
    # greedy approach, this solution may work for some but not all. 
    coins.sort()
    count = 0 
    for i in range(len(coins), -1, -1):
        while target > coins[i]:
            target -= coins[i]
            count += 1 

    return count 


# find minimum number of coins to reach a target n given a set of coins
# take 2. dynamic programming approach
def minCoins(coins, target): 
    dp = [sys.maxsize] * (target+1) 
    dp[0] = 0

    for i in range(1, target+1):
        for c in range(0, len(coins)):
            if coins[c] <= i: 
                currCount = dp[i - coins[c]]
                if currCount != sys.maxsize and currCount + 1 < dp[i]:
                    dp[i] = currCount + 1

    return dp[target] 

print(minCoins([25, 10, 5], 30)) # 2 
print(minCoins([9,6,5,1], 13)) # 3 
print(minCoins([1,3,5,7], 18)) # 4 

 



# return true if the given set of coins can sum up to a target
def coinSumsToTarget(coins, target):
    if target == 0:
        return True
    
    # dynamic programming approach to check if a given subset of coins sum up to a target and caching this 
    # ex: [1,2,3] and target = 6 
    # [3] with target 3 is a subproblem
    # [1,2] with target 3 is also a subproblem 
    # we notice that once we have a subarray that sums up to a target, we can re-use this value 
    # so then, the solutions is 
    # dp[i + c] = dp[i] 
    # this way we check every number possible up to this sum 
    dp = [False] * (target + 1) 
    dp[0] = True
    for i in range(0, target+1):
        for c in coins: 
           if dp[i] and i + c <= target:
               dp[i + c] = True
            
    
    return dp[target]



print(coinSumsToTarget([25, 10, 5], 30)) # True

print(coinSumsToTarget([7, 9], 8)) # False
print(coinSumsToTarget([1,3,5,7], 18)) # True
