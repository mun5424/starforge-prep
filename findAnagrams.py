class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p = sorted(p)
        
        res = []
        for i in range(0, len(s)-len(p)+1):
            sub = sorted(s[i:i+len(p)])
            if sub == p:
                res.append(i)
                
        return res
                
            