# No. 695

def max_area_of_island(grid: List[List[int]]) -> int:
    def get_area(i, j, grid, explored):
        if (i, j) in explored:
            return 0, explored
        
        explored[(i, j)] = None
        area = 1
        if i >= 1:
            if grid[i-1][j] == 1:
                new_area, explored = get_area(i-1, j, grid, explored)
                area += new_area
                
        if j >= 1:
            if grid[i][j-1] == 1:
                new_area, explored = get_area(i, j-1, grid, explored)
                area += new_area
                
        if i < len(grid) - 1:
            if grid[i+1][j] == 1:
                new_area, explored = get_area(i+1, j, grid, explored)
                area += new_area
                
        if j < len(grid[0]) - 1:
            if grid[i][j+1] == 1:
                new_area, explored = get_area(i, j+1, grid, explored)
                area += new_area
                
        return area, explored
    
    
    
    res = 0
    explored = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in explored:
                island_area, explored = get_area(i, j, grid, explored)
                res = max(res, island_area)
    return res

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]
]

max_area = max_area_of_island(grid)
print(max_area)
                
    
    