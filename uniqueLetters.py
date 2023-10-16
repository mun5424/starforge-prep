# find the maximum length of the substring where all letters are unique. 

def maxUniqueLetters(s): 
    uniques = {}
    n = len(s) 
    l, r = 0, 0
    maxLen = 0 
    # 0123456789
    # ABCDDDEFGHI
    while r < n: 
        if s[r] in uniques:
            l = max(l, uniques[s[r]] + 1)
        maxLen = max(maxLen, r-l + 1)
        uniques[s[r]] = r

        r += 1
