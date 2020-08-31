class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(node):
    if node is None:
        return
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=" ")

if __name__ == "__main__":
    root = TreeNode("F", TreeNode("B", TreeNode("A"), TreeNode("D", TreeNode("C"), TreeNode("E"))), TreeNode("G", None, TreeNode("I", TreeNode("H"))))

    print("\npreorder: ", end=" ")
    preorder(root)
    print("\ninorder: ", end=" ")
    inorder(root)
    print("\npostorder: ", end=" ")
    postorder(root)