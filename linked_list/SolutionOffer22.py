# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return head

        pre = head
        post = head
        for i in range(k):
            post = post.next
        while post!=None:
            pre=pre.next
            post= post.next

        return pre