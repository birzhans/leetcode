class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        
        a = b = idx = 0
        l1, l2 = len(matrix)-1, len(matrix[0])-1
        res = [0] * ((l1+1) * (l2+1))
        
        while (a <= l1 and b <= l2):
            for i in range(b,l2+1):
                res[idx] = matrix[a][i]
                idx += 1
            a += 1
            
            for i in range(a,l1+1):
                res[idx] = matrix[i][l2] 
                idx += 1
            l2 -= 1
            
            if a <= l1:
                for i in range(l2,b-1,-1):
                    res[idx] = matrix[l1][i]
                    idx += 1
                l1 -= 1
                
            if b <= l2:
                for i in range(l1,a-1,-1):
                    res[idx] = matrix[i][b]
                    idx += 1
                b += 1
                
        return res