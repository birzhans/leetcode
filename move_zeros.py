# No. 283
def moveZeroes(nums):
    j = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != j:
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums

 nums = [0,1,0,3,12,0,1]
 print(moveZeroes(nums))