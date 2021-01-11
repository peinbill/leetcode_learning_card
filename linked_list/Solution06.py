from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        returnlist = []
        current = head
        while current!=None:
            returnlist.insert(0,current.val)
            current = current.next
        return returnlist



