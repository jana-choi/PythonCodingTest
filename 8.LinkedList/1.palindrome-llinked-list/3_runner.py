class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    rev = None
    slow = fast = head

    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    
    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        rev, slow = rev.next, slow.next
    
    return not rev


if __name__ == "__main__":
    node_list1 = ListNode(1, ListNode(2))
    node_list2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print("1 > 2 :", isPalindrome(node_list1))
    print("1 > 2 > 2 > 1 :", isPalindrome(node_list2))
    node_list3 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    print("1 > 2 > 3 > 2 > 1 :", isPalindrome(node_list3))