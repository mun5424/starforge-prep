"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

from typing import List
import heapq
import math


"""
2 answers: 

1. keep a priority queue that has K closest points to the origin.
2. keep a list of the points with their sorted distances and return the top K

solution #1 sounds much more viable than 2 using less space O(k) over O(N)

"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = [] 
        for p in points:
            distance = -math.sqrt(p[1] * p[1] + p[0] * p[0])
            if len(pq) == k:
                heapq.heappushpop(pq, (distance, p))
            else:
                heapq.heappush(pq, (distance, p))

        return [tuple[1] for tuple in pq]
        