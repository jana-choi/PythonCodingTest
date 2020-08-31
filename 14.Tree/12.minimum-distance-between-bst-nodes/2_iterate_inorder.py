class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
import sys
def minDiffInBST(root):
    prev = -sys.maxsize
    result = sys.maxsize

    stack = []
    node = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        
        result = min(result, node.val - prev)
        prev = node.val

        node = node.right
    
    return result


if __name__ == "__main__":
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    root2 = TreeNode(10, TreeNode(4, TreeNode(1), TreeNode(8)), TreeNode(15))
    root3 = TreeNode(8, TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), TreeNode(12))

    print(minDiffInBST(root1))
    print(minDiffInBST(root2))
    print(minDiffInBST(root3))