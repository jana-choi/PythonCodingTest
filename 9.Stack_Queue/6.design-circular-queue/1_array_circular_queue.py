class MyCircularQueue:
    def __init__(self, k):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
    
    # enQueue(): 리어 포인터 이동
    def enQueue(self, value):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False
    
    # deQueue(): 프론트 포인터 이동
    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
    
    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    
    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None
    
    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None


if __name__ == "__main__":
    circular_queue = MyCircularQueue(5)
    print(circular_queue.enQueue(10))
    print(circular_queue.enQueue(20))
    print(circular_queue.enQueue(30))
    print(circular_queue.enQueue(40))
    print(circular_queue.Rear())
    print(circular_queue.isFull())
    print(circular_queue.deQueue())
    print(circular_queue.deQueue())
    print(circular_queue.enQueue(50))
    print(circular_queue.enQueue(60))
    print(circular_queue.Rear())
    print(circular_queue.Front())