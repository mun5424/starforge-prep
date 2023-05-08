"""
Coin change problem. Lots of variations

Given a set of coins, determine 
1. how many ways it can reach a sum n 
2. minimum number of coins to make n

"""

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



