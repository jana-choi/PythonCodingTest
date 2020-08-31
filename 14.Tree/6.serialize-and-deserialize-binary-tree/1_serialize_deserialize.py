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
        if nodes[index] is not "#":
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1

        if nodes[index] is not "#":
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1
    
    return root
    

if __name__ == "__main__":
    root = TreeNode("A", TreeNode("B"), TreeNode("C", TreeNode("D"), TreeNode("E")))
    str_s = serialize(root)
    print(str_s)
    print_tree(deserialize(str_s))