from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        # 요소 삽입 후 매 앞에 두는 상태로 재정렬
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0
        

if __name__ == "__main__":
    my_stack = MyStack()
    my_stack.push(1)
    my_stack.push(2)
    print(my_stack.top())
    print(my_stack.pop())
    print(my_stack.empty())