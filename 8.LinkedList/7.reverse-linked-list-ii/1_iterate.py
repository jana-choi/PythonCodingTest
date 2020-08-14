class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        s = str(self.val)
        s += " > " + self.next.__repr__() if self.next else ""
        return s

def reverseBetween(head, m, n):
    # 예외 처리
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head

    # start, end 지정
    for _ in range(m - 1):
        start = start.next
    end = start.next

    # 반복하면서 노드 차례대로 뒤집기
    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    
    return root.next

if __name__ == "__main__":
    node_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverseBetween(node_list, 2, 4))