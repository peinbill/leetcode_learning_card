# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list_setB = set()
        current_B = headB
        while current_B!= None:
            list_setB.add(current_B)
            current_B=current_B.next
        current_A = headA
        while current_A!=None:
            if current_A in list_setB:
                return current_A
            current_A=current_A.next
        return None