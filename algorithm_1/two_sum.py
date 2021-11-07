# No. 167

def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1
    
    while i < j:
        k = numbers[i] + numbers[j]
        if k == target:
            return [i+1, j+1]
        
        if k > target:
            j -= 1
        else:
            i+= 1


numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))
            
    
    