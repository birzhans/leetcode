# No. 35

def searchInsert(nums, target):
    i, j = 0, len(nums) - 1
    
    while i <= j:
        mid = (i + j) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return i
    