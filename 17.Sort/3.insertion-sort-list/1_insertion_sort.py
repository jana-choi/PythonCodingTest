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
    cur = parent = ListNode(None)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        cur.next, head.next, head = head, cur.next, head.next
        cur = parent
    return cur.next


if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(insertionSortList(head))