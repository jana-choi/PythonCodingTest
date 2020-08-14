class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        s = str(self.val)
        if self.next:
            s += " > " + self.next.__repr__()
        return s

def mergeTwoLists(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1


if __name__ == "__main__":
    l1 = ListNode(1, (ListNode(2, ListNode(4))))
    l2 = ListNode(1, (ListNode(3, ListNode(4))))
    print(mergeTwoLists(l1, l2))