class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, L, R):
    def dfs(node):
        if not node:
            return 0

        if node.val < L:
            return dfs(node.right)
        elif node.val > R:
            return dfs(node.left)
        return  node.val + dfs(node.left) + dfs(node.right)
    
    return dfs(root)


if __name__ == "__main__":
    root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    print(rangeSumBST(root, 7, 15))