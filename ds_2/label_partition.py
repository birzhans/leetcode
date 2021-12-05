class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = { c: i for i, c in enumerate(s) }
        last_index = start = 0
        ans = []
        
        for i, c in enumerate(s):
            last_index = max(last_index, last[c])
            if i == last_index:
                ans.append(i - start + 1)
                start = i + 1
                
        return ans
        