class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, L, R):
    if not root:
        return 0
    
    return (root.val if L <= root.val and root.val <= R else 0) + \
            rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R)


if __name__ == "__main__":
    root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    print(rangeSumBST(root, 7, 15))