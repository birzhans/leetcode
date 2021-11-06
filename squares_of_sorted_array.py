# No. 977

def sortedSquares(nums):
    l = len(nums)
    squared_nums = [0] * l
    i, j = 0, l - 1
    k = j
    while k >= 0:
        if abs(nums[i]) > abs(nums[j]):
            squared_nums[k] = nums[i]**2
            i += 1
        else:
            squared_nums[k] = nums[j]**2
            j -= 1
        k -= 1
    return squared_nums
            