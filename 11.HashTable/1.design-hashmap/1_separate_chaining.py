class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

from collections import defaultdict

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)

    def put(self, key, value):
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key):
        index = key % self.size

        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key):
        index = key % self.size

        if self.table[index].value is None:
            return -1

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 연결 리스트 노드 삭제
        prev, p = p, p.next
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next



if __name__ == "__main__":
    hash_map = MyHashMap()
    hash_map.put(1, 1)
    hash_map.put(2, 2)
    print(hash_map.get(1))
    print(hash_map.get(3))
    hash_map.put(2, 1)
    print(hash_map.get(2))
    hash_map.remove(2)
    print(hash_map.get(2))