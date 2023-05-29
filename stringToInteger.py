"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        n = 0
        i = 0
        sign = 1
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            i += 1
        
        while i < len(s):
            print(s[i])
            if not s[i].isdigit():
                i += 1
                break
                
            while i < len(s) and s[i].isnumeric():
                n *= 10
                n += int(s[i])
                i += 1
            break
            i += 1
        num = sign * n
        return max(-2 ** 31, num) if num < 0 else min (num, 2 ** 31-1)