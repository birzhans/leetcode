class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.val)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

'''
           1
       /       \
      2          3
    /           /  \
   4         None  None
  /  \
None None'''

print(root)