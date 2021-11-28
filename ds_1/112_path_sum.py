# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [[root, 0]]
        
        while stack:
            node, prevSum = stack.pop()
            if node:
                curr_val = node.val + prevSum
                if node.left == node.right == None and curr_val == targetSum:
                    return True
                
                stack.append([node.left, curr_val])
                stack.append([node.right, curr_val])
        
        return False
        