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

def insertionSortList(head):
    cur = parent = ListNode(0)  # 초기값 변경
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        cur.next, head.next, head = head, cur.next, head.next
        
        # 필요한 경우에만 cur 포인터가 되돌아가도록 처리 (다음번 head 가 cur 보다 큰 경우에는 돌아갈 필요 없음)
        if head and cur.val > head.val:
            cur = parent
    return parent.next


if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(insertionSortList(head))