class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
from collections import deque
def print_tree(root):
    if root is None:
        return

    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            print(cur.val, end=" ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        print("")
    print("")


from collections import deque
def invertTree(root):
    stack = deque([root])

    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left   # 전위 순회
            stack.append(node.left)
            stack.append(node.right)
    
    return root
    

if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    result = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))
    print_tree(root)
    print_tree(result)

    print_tree(invertTree(root))