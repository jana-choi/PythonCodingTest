class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        s = str(self.val)
        s += " > " + self.next.__repr__() if self.next else ""
        return s

def oddEvenList(head):
    # 예외 처리
    if head is None:
        return None
    
    odd = head
    even = even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
    
    odd.next = even_head

    return head

if __name__ == "__main__":
    node_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(oddEvenList(node_list))