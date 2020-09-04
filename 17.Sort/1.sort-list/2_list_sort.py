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

def sortList(head):
    # 연결 리스트 -> 파이썬 리스트
    p = head
    lst = []
    while p:
        lst.append(p.val)
        p = p.next
    
    # 정렬
    lst.sort()

    # 파이썬 리스트 -> 연결 리스트
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next
    
    return head


if __name__ == "__main__":
    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    print(sortList(head))
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(sortList(head))