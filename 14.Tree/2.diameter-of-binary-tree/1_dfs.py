class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root):
        def dfs(root):
            if root is None:
                return -1
                
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(root.left)
            right = dfs(root.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(Solution().diameterOfBinaryTree(root))