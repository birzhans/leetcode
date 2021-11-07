# No. 189

def rotate(nums, k):
    l = len(nums)
    k = k % l
    
    for i in range(l//2):
        nums[l-1-i], nums[i] = nums[i], nums[l-1-i]
        
    for i in range(k-1):
        nums[k-1-i], nums[i] = nums[i], nums[k-1-i]
        
    for i in range(k, (k+l)//2):
        nums[l-1-i+k], nums[i] = nums[i], nums[l-1-i+k]

    return nums