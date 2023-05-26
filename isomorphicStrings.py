

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map_t = {} 
        t_map_s = {} 
        
        for c1, c2 in zip(s,t):
            if (c1 not in s_map_t) and (c2 not in t_map_s):
                s_map_t[c1] = c2
                t_map_s[c2] = c1
                
            elif s_map_t.get(c1) != c2 or t_map_s.get(c2) != c1:
                return False 
    
        return True