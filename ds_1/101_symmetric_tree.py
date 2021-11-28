class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_nodes = [root.left]
        right_nodes = [root.right]
        
        while left_nodes and right_nodes:
            left_first = left_nodes.pop(0)
            right_first = right_nodes.pop(0)
            
            if left_first == right_first == None:
                pass
            
            elif left_first == None and right_first != None:
                return False
            elif left_first != None and right_first == None:
                return False
            
            else:
                if left_first.val != right_first.val:
                    return False

                left_nodes.append(left_first.left)
                left_nodes.append(left_first.right)

                right_nodes.append(right_first.right)
                right_nodes.append(right_first.left)
            
        return True
            