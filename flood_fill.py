# No. 733

def flood_fill(image, sr, sc, new_color):
    curr_color = image[sr][sc]
    
    if curr_color == new_color:
        return image
    
    image[sr][sc] = new_color
    
    if sr > 0:
        if image[sr-1][sc] == curr_color:
            image = flood_fill(image, sr-1, sc, new_color)
            
    if sc > 0:
        if image[sr][sc-1] == curr_color:
            image = flood_fill(image, sr, sc-1, new_color)
            
    if sr < len(image) - 1:
        if image[sr+1][sc] == curr_color:
            image = flood_fill(image, sr+1, sc, new_color)
            
    if sc < len(image[0]) - 1:
        if image[sr][sc+1] == curr_color:
            image = flood_fill(image, sr, sc+1, new_color)
    return image

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
new_color = 2

new_image = flood_fill(image, sr, sc, new_color)
