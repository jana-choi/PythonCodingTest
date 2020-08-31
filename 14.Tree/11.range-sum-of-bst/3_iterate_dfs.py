class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, L, R):
    stack, sum = [root], 0
    # 스택 이용 필요한 노드 DFS 반복
    while stack:
        node = stack.pop()
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val and node.val <= R:
                sum += node.val
    return sum


if __name__ == "__main__":
    root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    print(rangeSumBST(root, 7, 15))