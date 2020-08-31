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

def sortedArrayToBST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2

    # 분할 정복으로 이진 검색 결과 트리 구성
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid+1:])

    return node


if __name__ == "__main__":
    print_tree(sortedArrayToBST([-10, -3, 0, 5, 9]))