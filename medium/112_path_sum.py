# Given a binary tree, find if there is a root to leaf path that adds up to sum.


def findPath(tree, sum):
    if tree == None:
        return False

    if tree.val == sum and tree.left == None and tree.right == None:
        return True
    
    return findPath(tree.left, sum = tree.val) or findPath(tree.right, sum - tree.val)

    