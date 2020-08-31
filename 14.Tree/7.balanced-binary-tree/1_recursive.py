class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def deserialize(data):
    # 예외 처리
    if data == "# #":
        return None

    nodes = data.split()

    root = TreeNode(nodes[1])
    queue = deque([root])
    index = 2

    # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
    while queue:
        node = queue.popleft()
        if nodes[index] != "#":
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1

        if nodes[index] != "#":
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1
    
    return root

def isBalanced(root):
    def check(root):
        if not root:
            return 0
        
        left = check(root.left)
        right = check(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
    return check(root) != -1


if __name__ == "__main__":
    print(isBalanced(deserialize("# 3 9 20 # # 15 7 # # # #")))         # True
    print(isBalanced(deserialize("# 1 2 2 3 3 # # 4 4 # # # # # #")))   # False