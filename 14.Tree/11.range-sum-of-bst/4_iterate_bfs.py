class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, L, R):
    queue, sum = [root], 0
    # 큐 연산을 이용해 반복 구조 BFS로 필요한 노트 탐색
    while queue:
        node = queue.pop(0)
        if node:
            if node.val > L:
                queue.append(node.left)
            if node.val < R:
                queue.append(node.right)
            if L <= node.val and node.val <= R:
                sum += node.val
    return sum


if __name__ == "__main__":
    root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    print(rangeSumBST(root, 7, 15))