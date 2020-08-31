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

def buildTree(preorder, inorder):
    if inorder:
        # 전위 순회 결과는 중위 순회 분할 인덱스
        index = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[index])
        node.left = buildTree(preorder, inorder[:index])
        node.right = buildTree(preorder, inorder[index+1:])
        return node
    return None


if __name__ == "__main__":
    print(serialize(buildTree([3,9,20,15,7], [9,3,15,20,7])))
    print(serialize(buildTree([1,2,4,5,3,6,7,9,8], [4,2,5,1,7,9,6,8,3])))