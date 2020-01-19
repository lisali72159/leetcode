# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDepth(root):
    if root is None: return 0
    return 1 + min(minDepth(root.right), minDepth(root.left))

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b 
a.right = c 
c.left = d 
c.right = e

print minDepth(a)