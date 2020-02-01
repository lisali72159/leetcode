def LCA(root, p, q):
    if root is None: return None

    if p.val == root. val or q.val == root.val: return root

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if not left: return right
    if not right: return left

    return root

    LCA can be the root itself.
