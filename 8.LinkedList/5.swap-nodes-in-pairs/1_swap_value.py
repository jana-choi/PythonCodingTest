class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        s = str(self.val)
        s += " > " + self.next.__repr__() if self.next else ""
        return s

def swapPairs(head):
    cur = head
    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next
    return head


if __name__ == "__main__":
    node_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(swapPairs(node_list))