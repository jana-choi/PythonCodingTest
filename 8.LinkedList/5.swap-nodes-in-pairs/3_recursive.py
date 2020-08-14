class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        s = str(self.val)
        s += " > " + self.next.__repr__() if self.next else ""
        return s

def swapPairs(head):
    if head and head.next:
        p = head.next
        head.next = swapPairs(p.next)
        p.next = head
        return p

    return head


if __name__ == "__main__":
    node_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(swapPairs(node_list))