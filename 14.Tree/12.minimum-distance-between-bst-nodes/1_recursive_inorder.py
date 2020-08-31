class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import sys
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result


if __name__ == "__main__":
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    root2 = TreeNode(10, TreeNode(4, TreeNode(1), TreeNode(8)), TreeNode(15))
    root3 = TreeNode(8, TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), TreeNode(12))

    print(Solution().minDiffInBST(root1))
    print(Solution().minDiffInBST(root2))
    print(Solution().minDiffInBST(root3))