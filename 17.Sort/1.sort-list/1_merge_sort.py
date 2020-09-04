class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        result = str(self.val)
        node = self.next
        while node:
            result += " " + str(node.val)
            node = node.next
        return result

def mergeTwoList(l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = mergeTwoList(l1.next, l2)
    
    return l1 or l2

def sortList(head):
    if not (head and head.next):
        return head
    
    # 런너 기법 활용
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None

    # 분할 재귀 호출
    l1 = sortList(head)
    l2 = sortList(slow)

    return mergeTwoList(l1, l2)


if __name__ == "__main__":
    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    print(sortList(head))
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(sortList(head))