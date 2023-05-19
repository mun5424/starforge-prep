"""
Best time to buy and sell stock 

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""


from typing import List


def maxProfit(prices: List[int]) -> int:
    minSoFar = 1000000
    totalmax = -1
    currentprofit = -1 

    for p in prices:
        minSoFar = min(p, minSoFar) 
        currentprofit = max(p-minSoFar, currentprofit)
        totalmax = max(totalmax, currentprofit) 

    return totalmax 

print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1])) # 0


"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""


def maxProfit(self, prices: List[int]) -> int:
    minsofar = 1000000
    totalmax = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            totalmax += prices[i] - prices[i-1]
    
    return totalmax
        
