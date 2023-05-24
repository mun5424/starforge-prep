"""
merge intervals together i.e. [1,5] [3,6] -> [1,6] 

"""

from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x:x[0])
    
    # sorted by the first value of the intervals 
    # [3,5][2,4] -> [2,4][3,5] 

    n = len(intervals) - 1
    res = []
    for interval in intervals: 
        if not res or res[-1][1] < interval[0]:
            res.append(interval) 
        else:
            res[-1][1] = max(res[-1][1], interval[1])

        
    return res 