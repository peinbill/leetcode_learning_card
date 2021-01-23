class CQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def appendTail(self, value: int) -> None:
        self.stack1.push(value)

    def deleteHead(self) -> int:
        if len(self.stack1)==0:
            return -1
        while self.stack1.peek()!=None:
            self.stack2.push(self.stack1.pop())
        result = self.stack2.pop()
        while self.stack2.peek()!=None:
            self.stack1.push(self.stack2.pop())
        return result

class Stack:
    def __init__(self):
        self.que = []
    def push(self,value:int):
        self.que.append(value)
    def pop(self):
        return self.que.pop()
    def peek(self):
        if len(self.que)==0:
            return None
        return self.que[-1]
    def __len__(self):
        return len(self.que)


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()