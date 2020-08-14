class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        s = str(self.val)
        s += " > " + self.next.__repr__() if self.next else ""
        return s

def swapPairs(head):
    root = prev = ListNode(0)
    prev.next = head
    
    while head and head.next:
        # b가 a(head)를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head

        # prev가 b를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next

    return root.next


if __name__ == "__main__":
    node_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(swapPairs(node_list))