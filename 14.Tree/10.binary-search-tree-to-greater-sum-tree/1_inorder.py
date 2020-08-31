class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def serialize(root):
    queue = deque([root])
    result = ["#"]

    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)

            result.append(str(node.val))
        else:
            result.append("#")
    
    return " ".join(result)

class Solution:
    val = 0

    def bstToGst(self, root):
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        
        return root


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
    print(serialize(root))
    print(serialize(Solution().bstToGst(root)))