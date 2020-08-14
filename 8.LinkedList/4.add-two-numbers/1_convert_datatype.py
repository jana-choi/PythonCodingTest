class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        s = str(self.val)
        s += " > " + self.next.__repr__() if self.next else ""
        return s

class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head):
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node):
        to_list = list()
        while node:
            to_list.append(node.val)
            node = node.next
        return to_list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    
    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1, l2):
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int("".join(str(e) for e in a)) + int("".join(str(e) for e in b))

        # 최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))


if __name__ == "__main__":
    l1 = ListNode(2, (ListNode(4, ListNode(3))))
    l2 = ListNode(5, (ListNode(6, ListNode(4))))

    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))