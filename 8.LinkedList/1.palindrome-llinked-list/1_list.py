class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if not head:
        return True

    q = list()
    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next
    
    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    
    return True


if __name__ == "__main__":
    node_list1 = ListNode(1, ListNode(2))
    node_list2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print("1 > 2 :", isPalindrome(node_list1))
    print("1 > 2 > 2 > 1 :", isPalindrome(node_list2))