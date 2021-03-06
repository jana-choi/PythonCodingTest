class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)
    
    def pop(self):
        self.peek()
        return self.output.pop()
    
    def peek(self):
        # output 이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    def empty(self):
        return self.input == [] and self.output == []


if __name__ == "__main__":
    my_queue = MyQueue()
    my_queue.push(1)
    my_queue.push(2)
    print(my_queue.peek())
    print(my_queue.pop())
    print(my_queue.empty())