class Solution:
    def judgeCircle(self, moves: str) -> bool:
        uCount, rCount = 0, 0
        for s in moves: 
            if s == "U":
                uCount += 1
            elif s == "R":
                rCount += 1
            elif s == "L":
                rCount -= 1
            else:
                uCount -= 1
        
        return uCount == rCount == 0

    
                