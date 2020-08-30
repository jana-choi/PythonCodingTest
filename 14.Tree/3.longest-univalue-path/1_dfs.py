class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = 0

    def longestUnivaluePath(self, root):
        def dfs(root):
            if root is None:
                return 0
            
            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(root.left)
            right = dfs(root.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if root.left and root.left.val == root.val:
                left += 1
            else:
                left = 0
            
            if root.right and root.right.val == root.val:
                right += 1
            else:
                right = 0
            
            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)
        
        dfs(root)
        return self.result

if __name__ == "__main__":
    root1 = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))
    root2 = TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5)))
    print(Solution().longestUnivaluePath(root1))
    print(Solution().longestUnivaluePath(root2))
    root3 = TreeNode(4, TreeNode(4, TreeNode(4), TreeNode(4, None, TreeNode(4))), TreeNode(5, None, TreeNode(5)))
    print(Solution().longestUnivaluePath(root3))