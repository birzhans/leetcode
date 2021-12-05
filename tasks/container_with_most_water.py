class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = 0
        i, j = 0, len(height) - 1
        
        while i < j:
            if height[i] < height[j]:
                c = (j - i) * height[i]
                i += 1
            else:
                c = (j - i) * height[j]
                j -= 1
            r = max(r, c)
                
        return r
        