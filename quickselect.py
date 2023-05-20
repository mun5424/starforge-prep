"""
Quickselect is a root concept that QuickSort is based on. 
Divide and Conquer method where we use an arbitrary pivot.
could be any pivot, or we could use better mechanisms to find better pivots, but lets focus on the idea first

we move all items that are less than the pivot to the left, and move all greater to the right, eventually the list gets sorted. 
The reason why this method is powerful is because this can average out to be linear time O(n) 

any interview question that wants you to find the order of a certain element in an unsorted array, you can start thinking about quickselect. 

"""

# Find the smallest positive integer in an unsorted array
# assume that there is only one positive integer missing
# can include duplicates  
# [1,2,4] -> 3 
# [3,1,4] -> 2
# [1,1, 4, 3] -> 2


# this problem was something I couldnt really identify at the time but it happens to be a Leetcode-Hard problem.
# because eventually you will have to use Quickselect to reach linear time and constant space. 

from collections import defaultdict


def firstSmallestPositiveInt(nums):
    # first approach - use a HashSet
    if not nums:
        return None
    
    # add every count of element to the hashSet
    hashSet = defaultdict(int)
    for n in nums:
        hashSet[n]+= 1

    # from the minimum value, do +1 until we find the missing first positive

    currentVal = min(hashSet.keys())
    while True: 
        currentVal += 1
        if currentVal not in hashSet:
            return currentVal



print(firstSmallestPositiveInt([1,3,4])) # 2 
print(firstSmallestPositiveInt([-1, 0, 1, 1, 2, 4])) # 3 

# this solution works but interviewer will want something more efficient, 
# as this is O(n) runtime but uses O(n) space 

def partitionOnPivot(nums): 
    i = 0
    j = len(nums) -1 
    while i <= j: 
        if nums[i] <= 0:
            nums[i], nums[j] = nums[j], nums[i] 
            j = j - 1
        else:
            i = i + 1
    return i


def firstSmallestPositiveInt_quickselect(nums):
    if not nums:
        return None

    # partition the list so that all positive elements are on the left
    positiveEnd = partitionOnPivot(nums)
    print(nums) 
    print(positiveEnd)

    # flip all indexes of elements into negatives
    for i in range(positiveEnd):
        if abs(nums[i]) - 1 < positiveEnd and nums[abs(nums[i]) -1] > 0:
            nums[abs(nums[i]) - 1] *= -1 
    print(nums) 

    # the first positive element will be the missing integer
    for i in range(positiveEnd):
        if nums[i] > 0:
            return i + 1
        
    #edge case where last element happens to be missing 
    return positiveEnd + 1

# this works in O(n) time, O(1) space as there is no extra space called. 


print(firstSmallestPositiveInt_quickselect([1,3,4])) # 2 
print(firstSmallestPositiveInt_quickselect([-1, 0, 1, 1, 2, 4])) # 3 
print(firstSmallestPositiveInt_quickselect([-3, 1, 2, 5, 9, -4, -5])) # 3 


def firstMissingPositive(nums): 
    n = len(nums) 

    for i in range(n):
        if nums[i] < 1 or nums[i] > n:
            nums[i] = n + 1
    
    for i in range(n):
        val = abs(nums[i]) 
        if val > n: 
            continue
        if nums[val-1] > 0:
            nums[val-1] *= -1
        
    print(nums)
    for i in range(1, n):
        if nums[i] >= 0:
            return i + 1
    return n + 1
    


print("first missing positive with no quickselect")
print(firstMissingPositive([1,3,4])) # 2 
print(firstMissingPositive([1,2,3,4])) # 5 
print(firstMissingPositive([-1, 0, 1, 1, 2, 4])) # 3 


# this is how a quickselect would work, as reference
def partition(nums, l, r, pIndex):
    
    pivot = nums[pIndex]
    
    nums[pIndex], nums[r] = nums[r], nums[pIndex]
    pIndex = l 

    for i in range(r + 1): 
        if nums[i] <= pivot:
            nums[i], nums[pIndex] = nums[pIndex], nums[i] 
            pIndex += 1

    return pIndex - 1


def quickselect(nums, l, r, k):
    if l == r:
        return nums[l] 

    # choose a pivot - there are a lot of functions on how to choose a pivot efficiently 
    # but for sake of simplicity lets choose the rightmost element here
    pIndex = r
    pIndex = partition(nums, l, r, pIndex) 

    if pIndex == k:
        return nums[k] 
    elif pIndex < k:
        return quickselect(nums, pIndex+1, r, k) 
    return quickselect(nums, l, pIndex-1, k) 


def findKthLargest(nums, k):
    return quickselect(nums, 0, len(nums)-1, len(nums)-k) 


print(findKthLargest([5, 6, 1, 7, 9], 3)) # [1, 5, 6, 7, 9] 

