# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        if head.val == val:
            return head.next

        current = head
        next = current.next

        while next is not None:
            if next.val == val:
                current.next = next.next
                break
            else:
                current = next
                next=next.next

        return head