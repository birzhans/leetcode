class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        q = [[root, 0]]
        
        while q:
            last, index = q.pop(0)
            
            if last:
                if len(res) <= index:
                    res.append([last.val])
                else:
                    res[index].append(last.val)
                
                q.append([last.left, index+1])
                q.append([last.right, index+1])
        
        return res
