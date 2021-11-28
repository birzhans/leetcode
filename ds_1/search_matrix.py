def searchMatrix(matrix, target):
    i, j = 0, len(matrix) - 1
    l2 = len(matrix[0]) - 1

    # out range case
    if target < matrix[0][0] or target > matrix[j][l2]:
        return False

    # find row
    row = 0
    while i <= j:
        row = (i+j)//2
        
        if matrix[row][0] <= target <= matrix[row][l2]:
            break
        
        if target < matrix[row][0]:
            j = row - 1

        if  target > matrix[row][l2]:
            i = row + 1
            

    # find element
    i, j = 0, l2

    while i <= j:
        mid = (i+j)//2

        if matrix[row][mid] == target:
            return True

        if matrix[row][mid] < target:
            i = mid + 1
        else:
            j = mid - 1

    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target = 6

print(searchMatrix(matrix, target))