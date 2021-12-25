class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
        
    def helper(self, nums):
        l = len(nums)
        if l < 3:
            return max(nums)
        nums.insert(0, 0)
        for i in range(3, l+1):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2])