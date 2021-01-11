from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = list()
        push_index = 0

        for j in popped:
            while True:
                if len(stack)>0 and stack[0]==j:
                    stack.pop(0)
                    break
                else:
                    if push_index>=len(pushed):
                        return False
                    stack.insert(0,pushed[push_index])
                    push_index += 1


        return len(stack)==0