def maxDepth(root):
    if not root: return 0
    maximum = max(maxDepth(root.right), maxDepth(root.left))
    return 1 + maximum


def maxDepth2(root):
    if not root: return 0
    depth = 0
    queue = []

    while queue:
        depth += 1
        level = []
        if root.right: level.append(root.right)
        if root.left: level.append(root.left)
        queue = level

    return depth