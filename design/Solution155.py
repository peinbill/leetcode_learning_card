from collections import deque

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._deque = deque()
        self._min_deque = list()


    def push(self, x: int) -> None:
        self._deque.appendleft(x)
        self._min_deque.append(x)
        self._min_deque.sort()


    def pop(self) -> None:
        tmp = self._deque.popleft()
        self._min_deque.remove(tmp)

    def top(self) -> int:
        return self._deque[0]


    def getMin(self) -> int:
        return self._min_deque[0]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()