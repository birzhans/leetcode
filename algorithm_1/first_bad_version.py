# No. 278

def firstBadVersion(n):
    i, j = 0, n
    
    while True:
        m = (i + j) // 2
        
        if isBadVersion(m):
            if not isBadVersion(m-1):
                return m
            else:
                j = m - 1
        else:
            i = m + 1
            