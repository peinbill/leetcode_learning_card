# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        pre = None
        current = head
        next = head.next
        if next==None:
            return head

        while next!= None:
            current.next = pre
            pre = current
            current = next
            next = current.next
            current.next = pre

        return current

