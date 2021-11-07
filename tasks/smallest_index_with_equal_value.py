# No. 2057

def smallest_equal(nums):
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
        
    return -1

nums = [4,3,2,1]
print(smallest_equal(nums))