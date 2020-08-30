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


def mergeTrees(t1, t2):
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = mergeTrees(t1.left, t2.left)
        node.right = mergeTrees(t1.right, t2.right)
        return node
    else:
        return t1 or t2


if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    print_tree(mergeTrees(t1, t2))