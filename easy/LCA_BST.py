def LCA(root, p, q):
    if p.val < root.val: return LCA(root.left, p, q)
    if p.val > root.val: return LCA(root.right, p, q)

    return root.val