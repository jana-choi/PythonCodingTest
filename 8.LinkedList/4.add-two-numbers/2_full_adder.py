class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        s = str(self.val)
        s += " > " + self.next.__repr__() if self.next else ""
        return s

def addTwoNumbers(l1, l2):
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        # 두 입력값의 합 계산
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        
        # 몫(자리올림수)과 나머지(값) 계산
        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next
    
    return root.next

if __name__ == "__main__":
    l1 = ListNode(2, (ListNode(4, ListNode(3))))
    l2 = ListNode(5, (ListNode(6, ListNode(4))))
    print(addTwoNumbers(l1, l2))