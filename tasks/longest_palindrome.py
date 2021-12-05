class Solution:
    def longestPalindrome(self, s: str) -> int:
        r = c = 0
        d = {}
        
        for i in s:
            d[i] = d.get(i, 0) + 1
                
        for v in d.values():
            if v % 2 == 0:
                r += v
            else:
                r += v - 1
                c = 1
                
        
        return r + c
                
        
        