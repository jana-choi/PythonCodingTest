class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        s = str(self.val)
        s += " > " + self.next.__repr__() if self.next else " > NULL"
        return s

def reverseList(head):
    node, prev = head, None
    
    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    
    return prev


if __name__ == "__main__":
    node_list = ListNode(1, (ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    print(reverseList(node_list))
    print(node_list)